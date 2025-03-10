from fastapi import FastAPI
import math

app = FastAPI()

@app.get("/{num}")
async def factorial(num: int):
    return {"nfactorial": math.factorial(num)}
