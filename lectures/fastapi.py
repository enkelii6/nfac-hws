from contextlib import asynccontextmanager

from fastapi import FastAPI, status
from fastapi.responses import Response
import uvicorn

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # connect to database (for example)
    yield
    # disconnect from database


async def health():
    return Response(status_code=status.HTTP_200_OK)


app.add_api_route('/health', health)


if __name__ == '__main__':
    uvicorn.run('lectures.fastapi:app', port=8000, reload=True)
