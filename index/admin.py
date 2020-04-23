from django.contrib import admin
from .models import Authors, Book, Genre, BookFile, Quote, BookRead, Chapter

admin.site.register(Authors)
admin.site.register(Genre)
admin.site.register(BookFile)
admin.site.register(Book)
admin.site.register(Quote)
admin.site.register(BookRead)
admin.site.register(Chapter)