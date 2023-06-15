import virus_total
import uvicorn
from fastapi import FastAPI

app: FastAPI = FastAPI()
base_url: str = "/api/v3"
app.include_router(virus_total.router, prefix=base_url)

if __name__ == '__main__':
    uvicorn.run('virus_total_main:app', host='0.0.0.0', port=80, reload=True)
