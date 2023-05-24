from fastapi import FastAPI
from fastapi import File, UploadFile
import os
import code2flow as c2f

def server_clean(default_script, default_html):
    os.remove(default_script)
    os.remove(default_html)
    print("Server clean performed.")

app = FastAPI()

@app.post("/upload_script")
def upload(file: UploadFile = File(...)):
    # Temp upload of file to server to perform code2flow
    output_file = "temp.html"
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "Failed to upload file"}
    finally:
        html = c2f.code2flow([file.filename, "ktgfunc.py"], output_file)
        # We dont want to flood the server. Remove any created files
        server_clean(file.filename, output_file)
        file.file.close()
    return {"html": html}