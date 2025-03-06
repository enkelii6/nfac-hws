import asyncio
import os

import asyncpg

from lectures.repository import BaseRepository


class SQLRepository(BaseRepository):
    def __init__(self, table_name):
        self.table_name = table_name

    @property
    async def connection(self):
        return await asyncpg.connect(
            database=os.environ.get('DATABASE_NAME'),
            user=os.environ.get('DATABASE_USER'),
            password=os.environ.get('DATABASE_PASSWORD'),
            port=os.environ.get('DATABASE_PORT'),
            host=os.environ.get('DATABASE_HOST'),
        )

    async def get(self, **kwargs) -> dict:
        connection = await self.connection
        query = f'SELECT * FROM {self.table_name} WHERE '
        for key, val in kwargs.items():
            query += f'{key}="{val}"'

        return await connection.fetch(query)

    async def create(self, **kwargs) -> dict: ...

    async def update(self, **kwargs) -> dict: ...

    async def delete(self, **kwargs) -> dict: ...

    async def filter(self, **kwargs) -> [dict]: ...


sql_repository = SQLRepository('users')


async def main():
    await sql_repository.get(id=2)
    await sql_repository.get(name='Gleb')


if __name__ == '__main__':
    asyncio.run(main())
