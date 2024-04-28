import re

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")





if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
