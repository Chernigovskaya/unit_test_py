from unittest import TestCase
from unittest.mock import Mock
from book_service import BookService


class TestBookService(TestCase):
    mock_book = {'id': 3, 'name': 'Унесенные ветром'}
