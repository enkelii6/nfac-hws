from aiohttp import web

books = [
    {
        'id': '1',
        'title': '1984',
        'description': 'Book that changed the world',
        'rating': '4.99',
    },
]


async def handle(request):
    return web.json_response({'hello': 'world'})


app = web.Application()
app.add_routes([web.get('/', handle)])


if __name__ == '__main__':
    web.run_app(app)
