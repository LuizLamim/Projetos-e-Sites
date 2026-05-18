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

# 3. Rota GET básica (Página inicial)
@app.get("/")
def ler_raiz():
    return {"mensagem": "Olá, Mundo! Bem-vindo à minha API."}

# 4. Rota GET com parâmetro na URL
@app.get("/itens/{item_id}")
def ler_item(item_id: int):
    # O FastAPI converte automaticamente o item_id para inteiro (int)
    return {"item_id": item_id, "detalhes": "Aqui estariam os dados do banco de dados."}

# 5. Rota POST para receber e processar dados
@app.post("/itens/")
def criar_item(item: Item):
    # Aqui você normalmente salvaria o item no banco de dados
    return {
        "mensagem": f"O item '{item.nome}' foi recebido com sucesso!",
        "dados_recebidos": item
    }