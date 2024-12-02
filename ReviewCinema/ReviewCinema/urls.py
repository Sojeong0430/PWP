from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 페이지 URL
    path('', include('main.urls')),  # 메인 앱 URL
    path('common/', include('common.urls')),  # 로그인 등 공통 URL
    path('movies/', include('movie.urls')),  # 영화 앱 URL
    path('review/', include('review.urls')),
]
