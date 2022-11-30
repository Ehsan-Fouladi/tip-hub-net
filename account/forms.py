from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms
from .models import User
from django.core import validators

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label="گذرواژه", widget=forms.PasswordInput)
    password2 = forms.CharField(label='تکرار گذرواژه', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('number',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('number', 'password', 'is_active', 'is_admin')


# def phone_wite_0(value):
#     if value[0] != '0':
#         raise forms.ValidationError("شماره شما باید با صفر شروع بشود")

class FormLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"phone and email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"password"}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if len(username) > 50:
            raise ValidationError(
                '%(value)s شماره شما درست نمی باشد لطف دوباره تلاش کنید',
                code='invalid',
                params={'value':f'{username}'},
            )
        return username

    # def clean(self):
    #     cd = super().clean()
    #     number = cd['number']
    #     if len(number) > 12:
    #         raise ValidationError(
    #             'invalid value: %(value)s is invalid',
    #             code='invalid',
    #             params={'value':f'{number}'},
    #         )
    #     return number

class OtpLoginForm(forms.Form):
    number = forms.CharField(widget=forms.TextInput(attrs={"class":"email-input", "placeholder":"شماره تلفن"}), validators=[validators.MaxLengthValidator(12)])

class CzechOtpForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={"class":"password-input", "placeholder":"کد را وارد کنید "}), validators=[validators.MaxLengthValidator(4)])


class UserProFileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["number", "username", "image"]


class TeacherForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["author", "about_user", 'image']
        widgets={"image":forms.FileInput(attrs={"class":"form-control",}),}

        