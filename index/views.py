from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Authors, Book, Genre, BookFile, Quote, BookRead, Chapter

def index(request):
    books_popular = Book.objects.order_by('-view_count')[:15]
    books_visit = Book.objects.order_by('-visit_to')[:15]
    books_created = Book.objects.order_by('created_to')[:15]
    context = {
        'title' : 'Island of books',
        'books_popular' : books_popular,
        'books_visit' : books_visit,
        'books_created' : books_created,
    }
    return render(request, 'index/HomePage.html', context)

def author(request, id_author):
    author = Authors.objects.get(id=id_author)
    books = Book.objects.filter(authorbook__name = author.name)[:10]
    context = {
        'author' : author,
        'title' : author.name + ' - автор на сайте Island of Books, биография, книги',
        'books' : books,
    }
    return render(request, 'index/about_athor.html', context)



def author_list(request):
    chars = []
    for char in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ":
        b = Authors.objects.filter(name__startswith=char)
        if b:
            chars.append(char)
    context = {
        'title' : 'Авторы на сайте Island of Books',
        'chars' : chars,

        }
    return render(request, 'index/authors_list.html', context)


def book(request, id_book):
    book = Book.objects.get(id=id_book)
    return render(request, 'index/about_book.html', context={'book' : book, 'title' : book.title + ' - книга на сайте Island of Books, скачать, читать онлайн'})


def book_list(request):
    books = Book.objects.order_by('?')[:10]
    return render(request, 'index/book_list.html', context={'books' : books, 'title' : 'Книги на сайте Island of Books'})


def genre(request, id_genre):
    genre = Genre.objects.get(id=id_genre)
    books = Book.objects.filter(genre__title=genre.title).order_by('?')[:10]

    return render(request, 'index/about_genre.html', context={'title' : genre.title + ' - жанр на сайте Island of Books' ,'genre' : genre, 'books' : books})


def search(request):
    query = request.GET.get('search')
    #query = query[0].upper() + query[1:]

    result_book = Book.objects.filter(title__icontains=query)
    result_author = Authors.objects.filter(name__icontains=query)

    context = {
        'title' : query + ' - поиск по сайту Island of Books',
        'query' : query,
        'result_book' : result_book,
        'result_author' : result_author, 
    }
    return render(request, 'index/search.html', context)


def books_list(request):
    filt = request.GET.get('filt')
    if filt != "genre" and not("author" in filt):
        books = Book.objects.all()
        paginator = True
        if filt == "popular":
            books = books.order_by('-view_count')
        elif filt == "new_books":
            books = books.order_by('-created_to')
        elif filt == "visit_last":
            books = books.order_by('-visit_to')
        elif filt == "random":
            books.order_by('?')[:15]
        elif filt == "all":
            paginator = False
            chars = []
            for char in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ":
                b = books.filter(title__startswith=char)
                if b:
                    chars.append(char)
        elif "all" in filt:
            char = filt.split(' ')[1]
            books = books.filter(title__startswith=char).order_by('title')
        elif "genre" in filt:
            genre, char = filt.split(' ')[1:3]
            books = books.filter(genre__title=genre, title__startswith=char).order_by('title')
        else:
            paginator = False
            books = books.filter(genre__title=filt)
            chars = []
            for char in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ":
                b = books.filter(title__startswith=char)
                if b:
                    chars.append(char)

        if paginator:
            p = Paginator(books, 15)
            if "page" in request.GET:
                page = int(request.GET.get('page'))
            else:
                page = 1
            nt = page + 1
            if nt > p.num_pages:
                nt = 0
            lt = page - 1
            books = p.get_page(page)
            context={
                'books' : books,
                'pages' : [i for i in range(page-2, page+3) if i>0 and i<=p.num_pages],
                'page' : page, 
                'last' : lt, 
                'next' : nt,
                'type' : 'books',
                }
            return render(request, 'index/books-block.html', context)
        else:
            if "all" in filt:
                context = {
                    'chars' : chars,
                    'paginator' : 'no',
                    'type' : 'chars',
                    'author' : False,
                }
            else:
                context={
                    'chars' : chars,
                    'paginator' : 'no',
                    'type' : 'books',
                    'author' : False,
                    }
            return render(request, 'index/books-block.html', context)

    elif "author" in filt:
        context_set = False
        paginator = True
        if filt == "author":
            paginator = False
            chars = []
            for char in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ":
                b = Authors.objects.filter(name__startswith=char)
                if b:
                    chars.append(char)
        elif filt.split(' ')[1] == "x":
            name = filt.split(' ')[2] + ' ' + filt.split(' ')[3] + ' ' + filt.split(' ')[4]
            books = Book.objects.filter(authorbook__name=name)
            paginator = False
            chars = []
            for char in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ":
                b = books.filter(title__startswith=char)
                if b:
                    chars.append(char)
            context_set = True
            context = {
                    'chars' : chars,
                    'paginator' : 'no',
                    'type' : 'chars-b',
                    'author' : False,
                    'name' : name,
                }
        elif filt.split(' ')[1] == "X":
            name = filt.split(' ')[2] + ' ' + filt.split(' ')[3] + ' ' + filt.split(' ')[4]
            books = Book.objects.filter(authorbook__name=name, title__startswith=filt.split(' ')[5])
            p = Paginator(books, 15)
            if "page" in request.GET:
                page = int(request.GET.get('page'))
            else:
                page = 1
            nt = page + 1
            if nt > p.num_pages:
                nt = 0
            lt = page - 1
            books = p.get_page(page)
            context_set = True
            context={
                'books' : books,
                'pages' : [i for i in range(page-2, page+3) if i>0 and i<=p.num_pages],
                'page' : page, 
                'last' : lt, 
                'next' : nt,
                'type' : 'books',
                }
        else:
            authors = Authors.objects.filter(name__startswith=filt.split(' ')[1])
            p = Paginator(authors, 15)
            if "page" in request.GET:
                page = int(request.GET.get('page'))
            else:
                page = 1
            nt = page + 1
            if nt > p.num_pages:
                nt = 0
            lt = page - 1
            books = p.get_page(page)
            

        if paginator:
            if not context_set:
                context = {
                    'type' : 'authors',
                    'authors' : authors,
                    'pages' : [i for i in range(page-2, page+3) if i>0 and i<=p.num_pages],
                    'page' : page, 
                    'last' : lt, 
                    'next' : nt,
                }
        else:
            if not context_set:
                context = {
                    'paginator' : 'no',
                    'type' : 'chars',
                    'chars' : chars,
                    'author' : True,
                }
        return render(request, 'index/books-block.html', context)

    else:
        genres = Genre.objects.order_by('title')
        p = Paginator(genres, 15)
        if "page" in request.GET:
            page = int(request.GET.get('page'))
        else:
            page = 1
        nt = page + 1
        if nt > p.num_pages:
            nt = 0
        lt = page - 1
        context = {
            'genres' : p.get_page(page),
            'pages' : [i for i in range(page-2, page+3) if i>0 and i<=p.num_pages],
            'page' : page, 
            'last' : lt, 
            'next' : nt,
            'type' : 'genres',
        }
        return render(request, 'index/books-block.html', context)


def authors_list(request):
    query = request.GET.get('char')
    if query == "random":
        authors = Authors.objects.order_by('?')[:15]
    else:
        authors = Authors.objects.filter(name__startswith=query)
    p = Paginator(authors, 15)
    if "page" in request.GET:
        page = int(request.GET.get('page'))  
    else:
        page = 1
    nt = page + 1
    if nt > p.num_pages:
        nt = 0
    lt = page - 1     
    context = {
        'authors' : authors,
        'pages' : [i for i in range(page-2, page+3) if i>0 and i<=p.num_pages],
        'page' : page, 
        'last' : lt, 
        'next' : nt,
    }
    return render(request, 'index/author-block.html', context)



def get_quote(request):
    quote = Quote.objects.order_by('?')[0]
    return render(request, 'index/block-quote.html', context={'quote' : quote})
def get_book(request):
    book_site = request.GET.get('book').split('/')
    try:
        book_site = int(book_site[2])
        book = Book.objects.order_by('?')[0]
        if book.id == book_site:
            try:
                book = Book.objects.get(id=book.id+1)
            except:
                book = Book.objects.get(id=book.id-1)
    except:
        book = Book.objects.order_by('?')[0]
    return render(request, 'index/block_book.html', context={'book' : book})



def read_book(request, id_book_read):
    book = BookRead.objects.get(id=id_book_read)
    if book.chapter_set.count() == 1:
        return redirect('/chapter_read/' + str(book.chapter_set.get(number = 1).id))
    else:
        books = book.chapter_set.order_by('number')
        return render(request, 'index/book_read.html', context={'title': book.book.title + ' ' + book.title + ' - читать на сайте Island of Books', 'book': book, 'books' : books})


def read_chapter(request, id_chapter):

    chapter = Chapter.objects.get(id=id_chapter)
    try:
        Next = chapter.book_read.chapter_set.get(number=chapter.number + 1).id
    except:
        Next = 0
    
    try:
        Previos = chapter.book_read.chapter_set.get(number=chapter.number - 1).id
    except:
        Previos = 0

    context = {
        'title' : chapter.book_read.book.title + ' ' + chapter.book_read.title + ' - читать на сайте Island of Books',
        'chapter' : chapter,
        'next' : Next,
        'previos' : Previos,
    }
    return render(request, 'index/chapter_read.html', context)