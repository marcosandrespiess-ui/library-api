from pydantic import BaseModel, Field

class LivroSchema(BaseModel):
    titulo: str = Field(min_length=1, max_length=200)
    autor: str = Field(min_length=1, max_length=200)
    ano: int = Field(gt=0, lt=2100)
    genero: str = Field(min_length=1, max_length=100)
    paginas: int = Field(gt=0)
    editora: str = Field(min_length=1, max_length=200)
    edicao: int = Field(gt=0)