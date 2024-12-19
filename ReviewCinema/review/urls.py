from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('<int:movie_id>/', views.review_list, name='review_list'),  # 리뷰 목록 페이지
    path('<int:movie_id>/create/', views.review_create, name='review_create'),  # 리뷰 작성 페이지
    path('<int:movie_id>/delete/<int:review_id>/', views.review_delete, name='review_delete'),  # 리뷰 삭제
]
