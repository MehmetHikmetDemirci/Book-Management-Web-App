from django.test import TestCase
from .models import Book
from datetime import date

class BookModelTest(TestCase):

    def setUp(self):
        # Test için bir Book örneği oluştur
        Book.objects.create(
            title="Cesur Yeni Dunya",
            author="Aldous Huxley",
            published_date=date.today(),
            description="A test book description."
        )

    def test_book_creation(self):
        # Oluşturulan Book örneğini al
        book = Book.objects.get(title="Cesur Yeni Dunya")

        # Beklenen string temsili kontrol et
        self.assertEqual(str(book), "Cesur Yeni Dunya")

    def test_book_fields(self):
        # Oluşturulan Book örneğini al
        book = Book.objects.get(title="Cesur Yeni Dunya")

        # Alanların doğru şekilde ayarlandığını kontrol et
        self.assertEqual(book.author, "Aldous Huxley")
        self.assertEqual(book.description, "A test book description.")
        self.assertEqual(book.published_date, date.today())

