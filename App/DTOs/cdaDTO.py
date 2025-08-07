from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

class CdaDTO(BaseModel):
    num_cda: str
    ano_inscricao: int
    id_natureza_divida: int
    cod_situacao_cda: int
    data_situacao: datetime
    data_cadastramento: datetime
    cod_fase_cobranca: int
    valor_saldo: float

    @field_validator('num_cda')
    def validate_num_cda(cls, v):
        if not v.isdigit():
            raise ValueError('num_cda must be numeric')
        return v
    
    @field_validator('ano_inscricao')
    def validate_ano_inscricao(cls, v):
        if v < 1900 or v > datetime.now().year:
            raise ValueError('ano_inscricao must be a valid year')
        return v
    @field_validator('valor_saldo')
    def validate_valor_saldo(cls, v):
        if v < 0:
            raise ValueError('valor_saldo must be a non-negative number')
        return v