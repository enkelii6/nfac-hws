import asyncio

import aiohttp


async def get_google():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://0.0.0.0:8080', params={'example': 'Fight Club', 'sort': 'Year'}) as response:
            response_json = await response.json()
            print(response_json)


asyncio.run(get_google())
