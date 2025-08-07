from pydantic import BaseModel, ConfigDict, ValidationInfo, field_validator
from typing import Optional
from App.Enums.DocumentEnum import DocumentEnum

class PessoaDTO(BaseModel):
    id: int
    nome: str
    documento: Optional[str] = None
    tipo_documento: DocumentEnum

    @field_validator('nome')
    def validate_nome(cls, v):
        if not v.strip():
            raise ValueError('nome must not be empty')
        return v

    @field_validator('documento')
    def validate_documento(cls, v):
        if v is not None and not v.strip():
            raise ValueError('documento must not be empty if provided')
        return v

    @field_validator('tipo_documento', mode='before')
    def detect_document_type(cls, v, info: ValidationInfo):
        doc = info.data.get('documento')
        if not doc:
            raise ValueError('Campo "documento" está ausente ou é inválido')

        if len(doc) == 11:
            return DocumentEnum.CPF
        if len(doc) == 14:
            return DocumentEnum.CNPJ
    
        raise ValueError(f'documento inválido: deve ter 11 (CPF) ou 14 (CNPJ) dígitos: {doc}')