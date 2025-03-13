import uvicorn
from fastapi import FastAPI, Depends, Response

from seminar_task.dependencies import get_students_repo

app = FastAPI()


@app.get('/students')
async def list_students(repo = Depends(get_students_repo)):
    return Response(await repo.list())


# TODO: other endpoints


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=True)
