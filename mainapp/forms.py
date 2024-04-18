from django import forms
from django.db import models
from .models import Course, CategoryCourse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CategoryCourseForm(forms.ModelForm):
    name = forms.CharField(
        label='Название',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Название категории',
                'class': 'form-control'
            }
        )
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Описание',
                'class': 'form-control',
                'rows': 4,
                'cols': 20
            }
        )
    )

    class Meta:
        model = CategoryCourse
        fields = '__all__'


class CourseForm(forms.ModelForm):
    name = forms.CharField(
        label='Название',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Название курса',
                'class': 'form-control'
            }

        )
    )
    category = forms.ModelChoiceField(
        label='Направление курса',
        queryset=CategoryCourse.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            },
        )
    )
    teachers = forms.ModelMultipleChoiceField(
        label='Преподаватели',
        queryset=User.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'checkbox form-control'
            }
        )
    )
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Описание направления',
                'class': 'form-control',
                'rows': 4,
                'cols': 20
            }

        )
    )

    class Meta:
        model = Course
        fields = '__all__'


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('email уже зарегистрирован')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update()
            self.fields['email'].widget.attrs.update()
            self.fields['first_name'].widget.attrs.update()
            self.fields["last_name"].widget.attrs.update()
            self.fields['password1'].widget.attrs.update()
            self.fields['password2'].widget.attrs.update()
            self.fields[field].widget.attrs.update({"class": "form-control", "autocomplete": "off"})
