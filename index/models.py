from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


class Authors(models.Model):
    name = models.CharField(max_length = 120, db_index=True)
    biography = models.TextField(blank=True)
    img = models.ImageField(upload_to = 'foto/', blank=True)


    @property
    def photo_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

    def biog(self):
        return self.biography.split('\n')

    def __str__(self):
        return '{}'.format(self.name)


class Genre(models.Model):
    title = models.CharField(max_length= 120)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('genre', kwargs={'address' : self.address})


class Book(models.Model):
    title = models.CharField(max_length = 120, db_index=True)
    authorbook = models.ManyToManyField(Authors, blank=True)
    genre = models.ManyToManyField(Genre, blank=True)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers_book/', blank=True)

    view_count = models.IntegerField(default=0, editable=False)
    created_to = models.DateTimeField(auto_now_add=True)
    visit_to = models.DateTimeField(default=timezone.now() ,editable=False)
   

    def get_text(self):
        return self.description.split('\n')

    def view_plus(self):
        self.visit_to = timezone.now()
        self.view_count += 1
        self.save()
        return ''

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('book', kwargs={'address' : self.address})

    def save(self, *args, **kwargs):
        try:
            this = Book.objects.get(id=self.id)
            if this.cover != self.cover:
                this.cover.delete(save=False)
        except:
            pass
        super(Book, self).save(*args, **kwargs)

class BookFile(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title_read = models.CharField(max_length = 120, blank=True)
    title = models.CharField(max_length = 120)
    book_file = models.FileField(upload_to='books/')
    '''
    read_can = models.BooleanField(default=False)
    table_of_content = models.TextField(blank=True)
    '''

    def __str__(self):
        return 'Этот файл книги {}'.format(self.book.title) + ' '+ self.title

    '''
    def get_table_of_content(self):
        table = []
        for i in self.table_of_content.split('\n'):
            try:
                j = i.split('|')
                table.append([j[0], j[1].replace('\r', '')])
            except:
                table.append([i, 'none'])
        return table
    '''


class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=300)

    def __str__(self):
        return self.quote[:20] + '... - ' + self.author

class BookRead(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.book.title + ' ' + self.title

class Chapter(models.Model):
    book_read = models.ForeignKey(BookRead, on_delete=models.CASCADE)
    title_chapter = models.CharField(max_length=120)
    number = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.book_read.title + ' ' + self.title_chapter

    def get_text(self):
        return self.content.split('\n')