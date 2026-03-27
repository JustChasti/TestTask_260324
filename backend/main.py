import uvicorn
import os
from fastapi import FastAPI

from routes.base_router import router

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    port = int(os.getenv("APP_PORT", "8080"))
    uvicorn.run(app, host="0.0.0.0", port=port)
