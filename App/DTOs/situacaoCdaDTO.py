from pydantic import BaseModel, field_validator
from typing import Optional


class SituacaoCDADTO(BaseModel):
    cod_situacao_cda: int
    nome: str
    cod_situacao_fiscal: Optional[int]
    cod_fase_cobranca: Optional[int]
    cod_exigibilidade: Optional[int]
    tipo: Optional[str]

    @field_validator('nome')
    def nome_nao_vazio(cls, v):
        if not v.strip():
            raise ValueError('nome não pode ser vazio')
        return v

    @field_validator('tipo')
    def tipo_nao_vazio(cls, v):
        if v is not None and not v.strip():
            raise ValueError('tipo não pode ser vazio se fornecido')
        return v
