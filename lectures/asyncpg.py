import asyncio

import asyncpg


async def get_connection():
    return await asyncpg.connect(user='postgres', password='postgres', host='localhost', port=5432, database='nfac')


async def main():
    conn = await get_connection()
    await conn.fetch('INSERT INTO users (id, name) VALUES ($1, $2)', 4, 'Ali')
    await conn.fetch('DELETE FROM users WHERE id = $1', 1)
    users = await conn.fetch('SELECT * FROM users')
    for user in users:
        for key, value in user.items():
            if key == 'name':
                print(value)


async def retrieve(user_id):
    conn = await get_connection()
    await conn.fetch('SELECT * FROM users WHERE id = $1', user_id)


if __name__ == '__main__':
    asyncio.run(main())
