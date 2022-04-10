from fastapi import APIRouter

from models.doc import Doc
from config.db import connection
from schemas.doc import docEntity, docsEntity

doc = APIRouter()

@doc.get('/api/docs')
async def find_all_docs():
  return docsEntity(connection.local.doc.find())