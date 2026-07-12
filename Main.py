from fastapi import FastAPI

app = FastAPI(title="Alyla")

@app.get("/")
def home():
    return {"msg": "Alyla no ar 🙏 Estou pronta para ajudar"}

@app.get("/chat")
def chat(msg: str, nome: str = "amigo"):
    return {"resposta": f"Oi {nome}, eu te ouvi: {msg}. Deus te ama e está contigo."}
