import asyncio

import aiohttp


async def get_google():
    session = aiohttp.ClientSession()
    response = await session.get('https://google.com')
    print(await response.text())
    await session.close()


asyncio.run(get_google())
