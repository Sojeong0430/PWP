from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'director', 'genre', 'content']#,'total']  # 폼에 표시할 필드
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 40}),  # 줄거리 입력 칸
        # 'total': forms.NumberInput(attrs={'step': 0.5, 'min': 0, 'max': 5}),  # 평점 입력
        }
