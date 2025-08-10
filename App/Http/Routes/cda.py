from fastapi import APIRouter, Query, Depends
from App.Http.Requests.CdaResquest import CdaRequest
from typing import Annotated
from App.Http.Controllers.CdaController import CdaController

router = APIRouter(
    prefix="/cda",
    tags=["cdaRouter"],
    responses={404: {"description": "Cda routes not found"}}
)

@router.get("/search")
async def get_cdas(request: Annotated[CdaRequest, Depends()]):
    return CdaController.index(request)