from fastapi import FastAPI
app = FastAPI()

#endpoint her bir / afteri örnek olarak eğitimler/kurslar  buradaki kurslar bir endpointtir
@app.get("/") # burası path vermek içindir
async def HelloWorld(): #asenkron olarak çalıştırmak amacıyla
    return {"message": "Hello World"}

