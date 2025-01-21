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
    params_json = dict(request.query)
    # /?id=1&page=0 -> {'id': 1, 'page': 0}
    page = int(params_json.pop('page', 0))
    limit = int(params_json.pop('limit', 10))
    sort = params_json.pop('sort', 'rating')

    res = copy.deepcopy(books)
    if sort:
        res = await sort_books(res, sort)
    if params_json:
        res = await filter_books(res, **params_json)
    if page and limit:
        res = await paginate_books(res, page, limit)

    return web.json_response(res)


async def sort_books(books, sort_param):
    return books.sort(key = lambda book: book[sort_param])


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


async def paginate_books(books, page = 0, limit = 10):
    first = limit * page
    last = first + limit

    return books[first:last]


app = web.Application()
app.add_routes([web.get('/', handle)])
# 127.0.0.1:8080/?page=0&limit=1&title=1984


if __name__ == '__main__':
    web.run_app(app)
