from pydantic import BaseModel, Field, field_validator
from typing import Optional, Literal


class CdaRequest(BaseModel):
    numCDA: Optional[str] = Field(None, description="Número do CDA")
    minSaldo: Optional[float] = Field(None, ge=0, description="Saldo mínimo, deve ser >= 0")
    maxSaldo: Optional[float] = Field(None, ge=0, description="Saldo máximo, deve ser >= 0")
    minAno: Optional[int] = Field(None, ge=1900, le=2100, description="Ano mínimo, entre 1900 e 2100")
    maxAno: Optional[int] = Field(None, ge=1900, le=2100, description="Ano máximo, entre 1900 e 2100")
    natureza: Optional[str] = Field(None, max_length=50, description="Natureza do CDA")
    agrupamento_situacao: Optional[int] = Field(None, ge=0, description="Agrupamento da situação")
    sort_by: Optional[Literal["ano", "valor"]] = Field(None, description="Campo para ordenar: 'ano' ou 'valor'")
    sort_order: Optional[Literal["asc", "desc"]] = Field(default="asc", description="Ordem da ordenação: ascendente ou descendente")

    @field_validator('maxSaldo')
    def max_saldo_must_be_greater_than_min(cls, v, info):
        min_saldo = info.data.get('minSaldo')
        if v is not None and min_saldo is not None and v < min_saldo:
            raise ValueError('maxSaldo deve ser maior ou igual a minSaldo')
        return v

    @field_validator('maxAno')
    def max_ano_must_be_greater_than_min(cls, v, info):
        min_ano = info.data.get('minAno')
        if v is not None and min_ano is not None and v < min_ano:
            raise ValueError('maxAno deve ser maior ou igual a minAno')
        return v