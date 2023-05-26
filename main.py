from fastapi import FastAPI, status
from fastapi import File, UploadFile
import uuid
import os
import code2flow as c2f
from pydantic import BaseModel

class Request(BaseModel):
    script: str
    

def server_clean(default_script, default_html):
    if os.path.exists(default_script):
        os.remove(default_script)
    if os.path.exists(default_html):
        os.remove(default_html)

app = FastAPI()

@app.post("/upload_script")
def upload(request: Request):
    # Temp upload of file to server to perform code2flow
    output_file = "temp.html"
    try:
        filename = f"script{uuid.uuid4().hex}.py"
        with open(filename, 'w') as f:
            f.write(request.script)
        html = c2f.code2flow([filename, "ktgfunc.py"], output_file)
    except Exception:
        return {"message": "Failed to upload file"}#, status.HTTP_500_INTERNAL_SERVER_ERROR
    finally:
        # We dont want to flood the server. Remove any created files
        server_clean(filename, output_file)
    return {"html": html}