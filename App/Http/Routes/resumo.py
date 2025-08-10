from fastapi import APIRouter, Query, Depends
from App.Http.Requests.CdaResquest import CdaRequest
from typing import Annotated
from App.Http.Controllers.CdaController import CdaController


router = APIRouter(
    prefix="/resumo",
    tags=["resumoRouter"],
    responses={404: {"description": "Resumo routes not found"}}
)

@router.get("/distribuicao_cdas")
async def get_distribuicao():
    return CdaController.index_distribuicao_cda()

@router.get("/inscricoes")
async def get_inscricoes():
    return CdaController.index_inscricoes()