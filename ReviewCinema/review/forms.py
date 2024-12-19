from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']  # 리뷰 내용과 별점
        labels = {
            'content':'내용',
            'rating':'점수',
        }
        widgets={
            'rating':forms.Select(choices=[
                (1,'1점'),
                (2,'2점'),
                (3,'3점'),
                (4,'4점'),
                (5,'5점'),
            ])
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if not (1 <= rating <= 5):
            raise forms.ValidationError('점수는 1에서 5 사이여야 합니다.')
        return rating