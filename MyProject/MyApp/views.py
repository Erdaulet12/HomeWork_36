from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib.auth.models import User

# Create your views here.


def send_password_reset_emails(users):
	messages = []

	for user in users:
		reset_link = f"http://example.com/reset-password/{user.reset_token}"
		subject = "Восстановление пароля"
		body = f"""
        Здравствуйте, {user.username}!

        Для восстановления перейдите по следующей ссылке:
        {reset_link}

        """

		email = EmailMessage(
			subject=subject,
			body=body,
			from_email='erdauletakilzhan83@gmail.com',
			to=[user.email]
		)
		messages.append(email)

	for message in messages:
		message.send()


def send_password_reset_requests():
    users = User.objects.filter(is_active=True, reset_token__isnull=False)
    send_password_reset_emails(users)
