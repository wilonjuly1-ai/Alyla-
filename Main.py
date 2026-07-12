from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Alyla está online e pronta para evangelizar! 🙏"}

@app.get("/chat")
def chat(pergunta: str):
    return {"resposta": f"Alyla recebeu: {pergunta}. Em breve vou responder com a Palavra!"}
