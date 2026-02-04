from fastapi import FastAPI, Body
from datetime import datetime, time, timedelta
from uuid import UUID
from typing import Annotated

app = FastAPI()

# example of handling datetime, time, timedelta in request body 78aea7e5-97c3-4e77-92ea-d40d6a3a4439
@app.post("/process-datetime/{id}")
def process_datetime(
    id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time, Body()]
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "id": id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration
    }

