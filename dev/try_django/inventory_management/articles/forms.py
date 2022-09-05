from django import forms

from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data # it's a dictionary
        print(cleaned_data)
        title = cleaned_data.get('title')
        print(title)
        return title
    
    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     print('all data', cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower.strip() == 'the office':
    #         self.add_error('title', 'This Title is taken')
    #     return cleaned_data