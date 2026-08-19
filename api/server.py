from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def powitanie():
    return {"status": "sukces", "wiadomosc": "API dziala w nowym folderze!"}


@app.post("/columns")
def kolumny():
    return {"status": "sukces"}
