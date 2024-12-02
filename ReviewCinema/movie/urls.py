from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # 영화 목록 페이지
    path('add/', views.add_movie, name='add_movie'),  # 영화 추가 페이지
path('<int:pk>/delete/', views.delete_movie, name='delete_movie')
]
