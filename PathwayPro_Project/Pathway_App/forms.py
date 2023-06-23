from django import forms
# from captcha.fields import CaptchaField
from captcha.fields import ReCaptchaField

from django.db import models


class ChatForm(forms.Form):
    input1 = forms.CharField(label='Please Enter Your Current Job Title', max_length=200, required=False)
    input2 = forms.CharField(label='Please Enter Your Technical Skills', max_length=200, required=False)

    # captcha = CaptchaField()
    # captcha = ReCaptchaField()

    
    def clean(self):
        cleaned_data = super().clean()
        input1 = cleaned_data.get('input1')
        input2 = cleaned_data.get('input2')

        if input1 and input2:
            raise forms.ValidationError('Please enter only one field at a time.')

        if not input1 and not input2:
            raise forms.ValidationError('Please enter a value in either field.')

        return cleaned_data
    

# class Response(models.Model):
#     title = models.CharField(max_length=100)
#     skills = models.CharField(max_length=200)
#     tools = models.CharField(max_length=200)
#     # Add any other fields you need





