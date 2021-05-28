from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    year = models.IntegerField()
    description = models.CharField(max_length=1000)
    rating = models.CharField(max_length=10)
    ranking = models.IntegerField()
    review = models.CharField(max_length=2000)
    img_url = models.URLField()

    def get_absolute_url(self):
        return reverse("top_ten:movie-detail", kwargs={"id": self.id})