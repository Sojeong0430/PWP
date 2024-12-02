from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=50)  # 영화 제목
    director = models.CharField(max_length=20)  # 감독
    genre = models.CharField(max_length=10)  # 장르
    content= models.CharField(max_length=550)  # 줄거리
    total = models.DecimalField(max_digits=2, decimal_places=1)  # 총 평점

    class Meta:
        verbose_name = "영화"

    def __str__(self):
        return self.name
