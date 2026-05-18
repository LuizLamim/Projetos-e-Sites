from fastapi import FastAPI
from pydantic import BaseModel

# 1. Inicializa o aplicativo FastAPI
app = FastAPI(
    title="Minha API Básica",
    description="Um modelo inicial de API em Python"
)

# 2. Cria um modelo de dados para a requisição POST usando Pydantic
class Item(BaseModel):
    nome: str
    preco: float
    em_estoque: bool = True # Valor padrão