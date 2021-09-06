from django.shortcuts import render, redirect
from .forms import ContactForm
from decouple import config

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from django.contrib					import messages

def show_index(request):
	active = 1
	context = {
		'active' : active,
		'contact_form':ContactForm(),
 	}
	return render(request, 'baseapp/index.html', context)

def show_products(request):
	active = 2
	context = {
		'active' : active,
		'contact_form':ContactForm(),
 	}
	return render(request, 'baseapp/products.html', context)

def show_about(request):
	active = 3
	context = {
		'active' : active,
		'contact_form':ContactForm(),
 	}
	return render(request, 'baseapp/about.html', context)

def show_contacts(request):
	active = 4
	context = {
		'active' : active,
		'contact_form':ContactForm(),
 	}
	return render(request, 'baseapp/contacts.html', context)

def show_production(request):
	active = 5
	context = {
		'active' : active,
		'contact_form':ContactForm(),
 	}
	return render(request, 'baseapp/production.html', context)



def send_contact_form(request):

	if request.method == 'POST':

		contactForm = ContactForm(request.POST)

		if contactForm.is_valid():

			contactName = contactForm.cleaned_data['contactName']
			contactEmail = contactForm.cleaned_data['contactEmail']
			contactComment = contactForm.cleaned_data['contactComment']

			send_mail(contactName, contactEmail, contactComment)

			message = 'Форма обратной связи успешно отправлена.'
			messages.info(request, 'Форма обратной связи успешно отправлена.')

		else:

			message = 'Форма обратной связи заполнена некорректно. Попробуйте еще раз.'
			messages.info(request, 'Форма обратной связи заполнена некорректно. Подтвердите что вы не робот.')


	context = {
		'message' : message,
		'contact_form':ContactForm(),
 	}
	return render(request, 'baseapp/send_form_success.html', context)

def send_mail(name, email, comment):

	HOST = "mail.hosting.reg.ru"
	sender_email = config('MAIL_USER')
	receiver_email = ['info@annasoft.ru', 'shar.ltd31@yandex.ru', ]
	password = config('MAIL_PASSWORD')

	message = MIMEMultipart("alternative")
	message["Subject"] = "С Вами хотят связаться - {0}. e-mail {1}".format(name, email) 
	message["From"] = sender_email
	message["To"] = ','.join(receiver_email)

	text_body = """\
	"""

	html = """\
	<html>
      <body>
        <H3>С Вами хотят связаться - {0}. Email: {1}</H3>
        <p></p>
        <p>Комментарий:</p>
        <p>{2}</p>
      </body>
    </html>
	""".format(name, email, comment)

	part1 = MIMEText(text_body, "plain")
	part2 = MIMEText(html, "html")
	message.attach(part1)
	message.attach(part2)

	context = ssl.create_default_context()

	server = smtplib.SMTP(HOST, 587)
	server.starttls()
	server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email , message.as_string())
	server.quit()
