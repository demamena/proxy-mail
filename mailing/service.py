import email
import imaplib
import os
import random
import string

from django.core.mail import send_mail

from mailing.models import MailingUser


def create_username() -> str:
    while True:
        username = ''.join(random.SystemRandom().choice(string.digits) for _ in range(12))
        if not MailingUser.objects.filter(username=username).exists():
            return username


def create_mail_user(user_email: str, status: str) -> None:
    MailingUser.objects.create(email=user_email,
                               username=f'{status}-{create_username()}'
                                        f'@proxy.mail.vidodoguide.com')


def get_mailing_user_by_email(email_address: str) -> MailingUser:
    try:
        return MailingUser.objects.get(email=email_address)
    except Exception:
        pass


def get_mailing_user_by_username(username: str) -> MailingUser:
    try:
        return MailingUser.objects.get(username=username)
    except Exception:
        pass


def create_mail_files():
    create_virtual_file()
    create_external_file()


def create_virtual_file():
    with open('templates/virtual', 'w') as virtual:
        for user in MailingUser.objects.all():
            virtual.write(f'{user.username} {user.email}\n')


def create_external_file():
    with open('templates/external', 'w') as external:
        for user in MailingUser.objects.all():
            external.write(f'{user.email} {user.username}\n')
