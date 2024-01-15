from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel

from bing_service.bing_call import call_bing_bot, init_chatbot
# Create an instance of the FastAPI class
app = FastAPI()

# Serve static files (e.g., CSS, JavaScript)
app.mount("/static", StaticFiles(directory="static"), name="static")
# Use Jinja2 templates
templates = Jinja2Templates(directory="templates")


class CallPayload(BaseModel): 
    message: str

# Home route
@app.get("/")
async def read_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/init")
async def read_root():
    rs = await init_chatbot()
    return {"message": rs}

@app.post("/api/call")
async def process_message(call_payload: CallPayload):
    print('call_payload: ', call_payload.message)
    return await call_bing_bot(call_payload.message)

# Define another route with path parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}

@app.on_event("startup")
async def on_startup():
    # Initialize the chatbot during startup
    await init_chatbot()