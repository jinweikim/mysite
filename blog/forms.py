from django import forms
from pagedown.widgets import AdminPagedownWidget
from .models import Article

class LoginForm(forms.Form):
    uid = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','id':'uid','placeholder':'Username'}))
    pwd = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'pwd','placeholder':'Password'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label='userame',max_length=100,
                widget=forms.TextInput(attrs={'id':'username','class':'form-control','placeholder':'用户名','onblur':'authentication()'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'邮箱'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'密码'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'确认密码'}))

class SetInfoForm(forms.Form):
    username = forms.CharField()

class CommentForm(forms.Form):
    comment = forms.CharField(label='',widget=forms.Textarea(attrs={'cols':'60','rows':'6'}))

class SearchForm(forms.Form):
    keyword = forms.CharField(widget=forms.TextInput)

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Article
        fields = '__all__'