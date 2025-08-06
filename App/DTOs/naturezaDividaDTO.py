from pydantic import BaseModel, field_validator



class NaturezaDividaDTO(BaseModel):
    id: int
    nome: str
    descricao: str

    @field_validator('nome')
    def validate_nome(cls, v):
        if not v:
            raise ValueError('nome must not be empty')
        return v
