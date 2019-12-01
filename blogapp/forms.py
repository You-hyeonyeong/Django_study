from django import forms
from .models import Blog, Comment, User
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class CreateBlog(forms.ModelForm):
    class Meta:
        model = Blog

        fields = ['title', 'author', 'body']
        # 'widgets'을 지정하면, 장고에서 자체적으로 제공하는 폼의 형태를 빌려올 수 있습니다.
        # 'title'  TextInput가 형태가 맞는 형태이고, 'author'는 'Select'가  맞는 형태이므로 이를 적용하였습니다.
        # 'body'는 CKEditor 자체만의 위젯이 제공을 하므로 [CKEditorUploadingWidget]을 import하여 적용시켜주었습니다.
        # 입력 양식은 type은 기본이 text이다. 따라서 다르게 지정해주고 싶을 경우 widget을 이용한다.
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'author': forms.Select(
                attrs={'class': 'custom-select'},
            ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()),
        }


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['comment_textfield']
        widgets = {
            'comment_textfield': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40})
        }

