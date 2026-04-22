from pydantic import BaseModel, Field
from typing import List, Optional

class JogoSchema(BaseModel):
    nome: str = Field(min_length=1, max_length=200)
    ano: int = Field(gt=1950, lt=2100)
    desenvolvedora: str = Field(min_length=1, max_length=200)
    subgenero: Optional[str] = Field(min_length=1, max_length=100)
    plataformas: List[str] = Field(default_factory=list)
    generos: List[str] = Field(default_factory=list)        
    modos: List[str] = Field(default_factory=list)
    