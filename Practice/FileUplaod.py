# wokring with file upload
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import HTMLResponse
from typing import Annotated

app = FastAPI()

# upload by using File
@app.post("/file/")
async def create_file(file: Annotated[bytes, File()]):
    return {"fileSize": len(file)}

# upload and read files
@app.post("/uploadFile")
async def upload_file(files: UploadFile):
    if files.content_type == "text/plain":
        content = await files.read()
    return {"file_name": files.filename, "content_type": files.content_type, "content": content }

# Optional file uplaod
@app.post("/optional-file/")
async def multi_upload_files(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {"message": " No file uploaded"}
    return {"file_size":  len(file)}


# optional uploadfiles and metadata
@app.post("/optional-upload-files", summary="Optional upload feature", description="With this endpoint you can uload only valid documents.")
async def optional_file_upload(files: UploadFile | None = None):
    if not files:
        return {"message": " No file uploaded"}
    else:
        return {"file_name": files.filename, "content_type": files.content_type }


# Multi file uplaod feature by using file
@app.post("/multi-file-uplaod/", summary="Handle multiple files by File")
async def multi_file_upload(file: Annotated[list[bytes], File(description="Multiple files by File")]):
    return {"filesize": [ len(value) for value in file]}


# Multi file handle by UploadFiles
@app.post("/multi-upload-files/", summary="handle multi files by UploadFiles")
async def multi_uplaod_files(files: Annotated[list[UploadFile], File(description="Multiple file as UploadFiles")] ):
    if len(files) < 1:
         HTTPException(status_code=401, detail="Not found")
    return { "filenames": [value.filename.capitalize() for value in files] }

# html endpoint for multifile uplaod
@app.get("/html-form-multi-file")
async def html_multi_form ():
    content  = """
<body>
<form action="/multi-file-uplaod/" enctype="multipart/form-data" method="post">
<input name="file" type="file" multiple>
<input type="submit">
</form>
<form action="/multi-upload-files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
"""
    return HTMLResponse(content)

# Use form field and file data in same form
@app.post("/sumit-form-data/")
async def submit_form_data(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()],
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }