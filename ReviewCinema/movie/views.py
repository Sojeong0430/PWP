from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm  # MovieForm 임포트

# 영화 추가 뷰
def add_movie(request):
    if request.method == 'POST':  # 폼 제출 시
        form = MovieForm(request.POST)  # 제출된 데이터로 폼 생성
        if form.is_valid():  # 데이터가 유효한지 검증
            movie_instance = form.save(commit=False)  # 폼 저장을 지연
            movie_instance.total = 0.0  # 기본 total 값 설정
            movie_instance.save()  # 데이터 저장
            return redirect('movie:movie_list')  # 영화 목록 페이지로 이동
    else:  # 폼을 처음 요청할 때
        form = MovieForm()  # 빈 폼 생성
    return render(request, 'movie/add_movie.html', {'form': form})  # 폼 렌더링

# 영화 목록 보기 뷰
def movie_list(request):
    movies = Movie.objects.all()  # DB에서 모든 영화 가져오기
    return render(request, 'movie/movie_list.html', {'movies': movies})

# 영화 삭제 뷰
def delete_movie(request, pk):
    movie_to_delete = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie_to_delete.delete()
        return redirect('movie:movie_list')
    return render(request, 'movie/confirm_delete.html', {'movie': movie_to_delete})
