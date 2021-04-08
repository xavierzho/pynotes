from django import forms
import re


class RegInfo(forms.Form):
    username = forms.CharField(min_length=4, max_length=16,
                               error_messages={'min_length': '用户名最小4位',
                                               'max_length': '用户名最大16位',
                                               },
                               label='用户名'
                               )
    email = forms.EmailField()
    password = forms.CharField(min_length=8, max_length=12,
                               error_messages={
                                   'min_length': '密码最小8位',
                                   'max_length': '密码最大12位',
                               },
                               label='密码'
                               )
    confirm_password = forms.CharField(min_length=8, max_length=12,
                                       error_messages={
                                           'min_length': '确认密码最小8位',
                                           'max_length': '确认密码最大12位',
                                       },
                                       label='确认密码'
                                       )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        patten = re.compile("^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,12}$")
        is_valid = patten.match(password)
        if not is_valid:
            self.add_error(password, '密码必须以大或小写字母开头，必须包含一个大小字母，一个小写字母，一个数字')
        return password

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not password == confirm_password:
            self.add_error(confirm_password, '两次密码不相同')
        return self.cleaned_data
