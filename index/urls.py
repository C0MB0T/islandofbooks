from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books$', views.book_list, name='book_list'),
    url(r'^books/(?P<id_book>[0-9]+)/$', views.book, name='Detail_Book'),
    url(r'^authors/$', views.author_list, name="author_list"),
    url(r'^authors/(?P<id_author>[0-9]+)/$', views.author, name='Detail_Author'),
    url(r'^genre/(?P<id_genre>[0-9]+)/$', views.genre, name='Detail_Genre'),
    url(r'^search$', views.search, name='Search'),
    url(r'^books_list/$', views.books_list),
    url(r'^book_read/(?P<id_book_read>[0-9]+)$', views.read_book, name='ReadBook'),
    url(r'^chapter_read/(?P<id_chapter>[0-9]+)$', views.read_chapter, name='ReadChapter'),
    url(r'^authors_list/$', views.authors_list),
    url(r'^get_quote/$', views.get_quote),
    url(r'^get_book/$', views.get_book),
]
