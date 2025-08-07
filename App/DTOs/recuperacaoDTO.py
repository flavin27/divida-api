from pydantic import BaseModel, field_validator
from typing import Literal

class RecuperacaoDTO(BaseModel):
    num_cda: str
    prob_recuperacao: float
    sts_recuperacao: int

    @field_validator('num_cda')
    def validate_num_cda(cls, v):
        if not v.isdigit():
            raise ValueError('num_cda must be numeric')
        return v
    @field_validator('prob_recuperacao')
    def validate_prob_recuperacao(cls, v):
        if (v < 0):
            raise ValueError('prob_recuperacao must be a non-negative number')
        return v
    @field_validator('sts_recuperacao')
    def validate_sts_recuperacao(cls, v):
        if v not in [0, 1]:
            raise ValueError('sts_recuperacao must be either 0 (não recuperado) or 1 (recuperado)')
        return v