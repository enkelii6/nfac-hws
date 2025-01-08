emails = ['', '', 'bauka@maill.com', 'niyaz@gmail.com', '']

emails = [email for email in emails if email]

print(emails)


def example(books):
    return [{
        'id': book.id,
        'title': book.title,
    } for book in books]


def example_with_for(books):
    result = []

    for book in books:
        result.append({
            'id': book.id,
            'title': book.title,
        })

    return result
