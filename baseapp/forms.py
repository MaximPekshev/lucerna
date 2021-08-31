from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.Form):
	
	contactName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
			'class': 'textfield',
			'placeholder': 'Ваше Имя',
			'id': 'contactNameInput',

		}))
	contactEmail = forms.EmailField(max_length=30, widget=forms.TextInput(attrs={
			'class': 'textfield',
			'placeholder': 'E-mail',
			'id': 'contactEmailInput',
		}))
	contactComment = forms.CharField(max_length=1024, required=False, widget=forms.Textarea(attrs={
			'class': 'textfield',
			'placeholder': 'Сообщение',
			'id': 'contactCommentInput',
			'rows': '5',
		}))
	captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)