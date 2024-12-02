from django.db import models
from movie.models import Movie
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=50) #제목
    content = models.CharField(max_length=500) #내용
    rating = models.DecimalField(max_digits=2,decimal_places=1) #별점
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews') #영화
    user = models.ForeignKey(User, on_delete=models.CASCADE) #글쓴이

    class Meta:
        verbose_name = "리뷰"