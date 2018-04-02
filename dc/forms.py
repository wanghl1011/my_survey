from django import forms
from django.forms import widgets
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from dc.models import *
class Ques_modelform(ModelForm):
    class Meta:
        choices = (
            (1, "评分"),
            (2, "描述"),
            (3, "单选"),
        )
        model=Question
        fields=["title","type"]
        widgets ={
            "title":widgets.Textarea(attrs={"class": "form-control", "rows": "2"}),
            "type":widgets.Select(attrs={"class": "form-control type"}, choices=choices)
        }
class Option_modelform(ModelForm):
    class Meta:
        model=Option
        fields=["name","score"]
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control"}),
            "score": widgets.NumberInput(attrs={"class": "form-control"})
        }

# class UserInfo_modelform(ModelForm):
#     class Meta:
#         model=UserInfo
#         fields=["username",]
#         widgets = {
#             "username": widgets.TextInput(attrs={"class": "form-control"}),
#         }
# class Grade_modelform(ModelForm):
#     class Meta:
#         model=Grade
#         fields=["name",]
#         widgets = {
#             "name": widgets.TextInput(attrs={"class": "form-control"}),
#         }
class Questionnaire_modelform(ModelForm):
    class Meta:
        model=Questionnaire
        fields=["title", "grade", "create_user"]
        widgets = {
            "title": widgets.TextInput(attrs={"class": "form-control"}),
            "grade": widgets.Select(attrs={"class": "form-control"}),
            "create_user": widgets.Select(attrs={"class": "form-control"}),
        }














class Ques_form(forms.Form):
    # def __init__(self,request,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.request=request
    question=forms.CharField(
        max_length=32,
        error_messages={
            "min_length": "问题名称长度过短",
            "max_length": "问题长度名长度过长",
            "required": "问题名称不能为空"
        },
        widget=widgets.Textarea(attrs={"class": "form-control", "rows": "2"})
    )
    choices = (
        (1, "评分"),
        (2, "描述"),
        (3, "单选"),
    )
    type=forms.IntegerField(
        error_messages={
            "min_length": "密码长度过短",
            "required": "密码不能为空"
        },
        widget=widgets.Select(attrs={"class": "form-control type"}, choices=choices)
    )
    # repassword=forms.CharField(
    #     min_length=9,
    #     error_messages={
    #         "min_length":"密码长度过短",
    #         "required":"密码不能为空"
    #     },
    #     widget = widgets.PasswordInput(attrs={"class": "form-control","placeholder":"重新输入密码"})
    # )
    # email=forms.EmailField(
    #     error_messages={
    #         "required":"邮箱不能为空",
    #         "invalid":"邮箱格式错误"
    #     },
    #     widget=widgets.TextInput(attrs={"placeholder":"邮箱地址","class": "form-control"})
    # )
    # check_code=forms.CharField(
    #     error_messages={
    #         "required": "验证码不能为空",
    #     },
    #     widget=widgets.TextInput(attrs={"placeholder": "请输入右边图片中的验证码", "class": "form-control"})
    # )



    # def clean_username(self):
    #     username = self.cleaned_data.get("username")
    #     user = UserInfo.objects.filter(username=username).first()
    #     if user:
    #         raise ValidationError("该用户已存在")
    #     else:
    #         return self.cleaned_data.get("username")
    # def clean_password(self):
    #     if self.cleaned_data.get("password").isdigit():
    #         raise ValidationError("密码不能为纯数字")
    #     elif self.cleaned_data.get("password").isalpha():
    #         raise ValidationError("密码不能为纯字母")
    #     else:
    #         return self.cleaned_data.get("password")
    # def clean_check_code(self):
    #     if self.cleaned_data.get("check_code").upper()==self.whl.upper():
    #         return self.cleaned_data.get("check_code")
    #     else:
    #         raise ValidationError("验证码输入不正确")
    # def clean(self):
    #     if self.cleaned_data.get("password"):
    #         if self.cleaned_data.get("password") == self.cleaned_data.get("repassword"):
    #             return self.cleaned_data
    #         else:
    #             raise ValidationError("密码输入不一致")
    #     else:
    #         return self.cleaned_data

