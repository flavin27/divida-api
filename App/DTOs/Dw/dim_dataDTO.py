from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

class DimDataDTO(BaseModel):
    data: datetime
    ano: int
    mes: int
    dia: int
    trimestre: int
    semana: int
    dia_semana: int

    @field_validator('data')
    def validate_data(cls, v):
        if not isinstance(v, datetime):
            raise ValueError('data must be a valid datetime object')
        return v

    @field_validator('ano', 'mes', 'dia', 'trimestre', 'semana', 'dia_semana')
    def validate_numeric_fields(cls, v):
        if not isinstance(v, int) or v < 0:
            raise ValueError('Field must be a non-negative integer')
        return v
    @field_validator('mes')
    def validate_mes(cls, v):
        if v < 1 or v > 12:
            raise ValueError('mes must be between 1 and 12')
        return v
    @field_validator('dia')
    def validate_dia(cls, v):
        if v < 1 or v > 31:
            raise ValueError('dia must be between 1 and 31')
        return v
    @field_validator('trimestre')
    def validate_trimestre(cls, v):
        if v < 1 or v > 4:
            raise ValueError('trimestre must be between 1 and 4')
        return v
    @field_validator('semana')
    def validate_semana(cls, v):
        if v < 1 or v > 53:
            raise ValueError('semana must be between 1 and 53')
        return v
    @field_validator('dia_semana')
    def validate_dia_semana(cls, v):
        if v < 0 or v > 6:
            raise ValueError('dia_semana must be between 0 (Sunday) and 6 (Saturday)')
        return v
    