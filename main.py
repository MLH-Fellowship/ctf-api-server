from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Take my flag", "flag": "mlh{g1t_3quals_bl4ck_m4g1c}"}
