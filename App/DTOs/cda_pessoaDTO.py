from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

class Cda_pessoaDTO(BaseModel):
    num_cda: str
    idPessoa: int
    sitacao_devedor: int

    @field_validator('num_cda')
    def validate_num_cda(cls, v):
        if not v.isdigit():
            raise ValueError('num_cda must be numeric')
        return v
    @field_validator('sitacao_devedor')
    def validate_sitacao_devedor(cls, v):
        if v not in [1,2,3]:
            raise ValueError('sitacao_devedor must be either 1, 2, or 3')
        return v
    @field_validator('idPessoa')
    def validate_idPessoa(cls, v):
        if v < 0:
            raise ValueError('idPessoa must be a non-negative number')
        return v