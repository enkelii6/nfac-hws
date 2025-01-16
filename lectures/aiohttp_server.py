from aiohttp import web

books = [
    {
        'id': 1,
        'title': '1984',
        'description': 'Book that changed the world',
        'rating': '4.99',
    },
    {
        'id': 2,
        'title': 'Fight Club',
        'description': 'Man with schizofrenia trying to socialize',
        'rating': '1.21',
    }
]


async def handle(request):
    params_json = dict(request.rel_url.query)

    return web.json_response(await filter_books(books, **params_json))


async def filter_books(books, **filters):
    filtered_books = []
    for book in books:
        for key, value in filters.items():
            try:
                if book[key] == value:
                    filtered_books.append(book)
            except KeyError:
                continue

    return filtered_books


app = web.Application()
app.add_routes([web.get('/', handle)])


if __name__ == '__main__':
    web.run_app(app)
