books = [
    {
        'id': 1,
        'name': 'Закон джунглей',
    },
    {
        'id': 2,
        'name': 'Родная кровь',
    },
]


def fetch_books(id, books):
    for book in books:
        if book['id'] == id:
            return book


print(fetch_books(1, books))
