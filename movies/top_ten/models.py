from django.db import models
from django.urls import reverse
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    year = models.IntegerField()
    description = models.CharField(max_length=1000)
    rating = models.CharField(max_length=10)
    ranking = models.IntegerField()
    review = models.CharField(max_length=2000)
    img_url = models.URLField(max_length=20000)
    owner = models.ForeignKey('auth.user', related_name='movies', on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        title = 'table' if self.title else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(id=self.id, linenos=title,
                                  full=True, **options)
        super(Movie, self).save(*args, **kwargs)



class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to='media')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# class User()