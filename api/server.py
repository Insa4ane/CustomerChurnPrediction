from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def powitanie():
    return {"status": "sukces", "wiadomosc": "API dziala w nowym folderze!"}
