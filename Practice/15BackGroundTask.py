# background task

from fastapi import FastAPI, BackgroundTasks, Query, Depends
from typing import Annotated
from asyncio import sleep

app = FastAPI()

def writing_notification(email: str, text: str):
    with open("output.txt", "a") as f:
        f.write(f"notification for {email}: {text} \n")

async def writing_email(email: str, text: str):
    with open("output.txt", mode="w") as email_file:
        email_file.write(f"email for {email}: {text} from notification api \n")

# notification message append email message in output.txt because of mode="a". a means append.
@app.post("/send-notification/")
async def send_notification(backgound_tasks: BackgroundTasks, email: str, text: str):
    backgound_tasks.add_task(writing_notification, email, text)
    return {"message": "Notification send in background"}

# notification message overwrite email message in output.txt because of mode="w". w means write and overwrite the file.
@app.post("/notification/{email}")
async def send_notification(backgound_tasks: BackgroundTasks, email: str, text: str):
    backgound_tasks.add_task(writing_email, email, text)
    return {"message": "Notification send in background"}

# Background tasks can be used as dependencies. we just need use .add_task(), first parameter is the function and the rest of parameters are the parameters of that function. 
def write_log(message: str):
    import time
    time.sleep(3)
    with open("output.txt", mode="a") as log_file:
        log_file.write(f"message: {message} \n")

def get_query(background_tasks: BackgroundTasks, query: str | None = None):
    if query:
        message = f"query received: {query}"
        background_tasks.add_task(write_log, message)
    return query

@app.get("/items/")
async def read_items(background_tasks: BackgroundTasks, query: Annotated[str | None, Depends(get_query)] ):
    message = f"read items with query: {query}"
    background_tasks.add_task(write_log, message)
    return {"name" : "item", "query": query}