from django.forms import ModelForm
from thjDjango.Books.models import Book

# Create the form class.
class BookForm(ModelForm):
    class Meta:
        model = Book
