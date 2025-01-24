from db.models import init_db
from tg_bot.bot import main
import uvicorn
from fastapi import FastAPI
from back.api import api_router

app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    # asyncio.run(init_db())
    # uvicorn.run(app, host="0.0.0.0", port=8000)