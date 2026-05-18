from fastapi import FastAPI
from pydantic import BaseModel

# 1. Inicializa o aplicativo FastAPI
app = FastAPI(
    title="Minha API Básica",
    description="Um modelo inicial de API em Python"
)