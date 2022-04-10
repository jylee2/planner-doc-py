from fastapi import FastAPI

from routes.doc import doc

app = FastAPI()
app.include_router(doc)