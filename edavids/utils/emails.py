from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string


def send_message(email, message):
    c = Context({"email": email, "message": message})

    email_subject = render_to_string(
        "emails/contact/send_message_subject.txt", c
    ).replace("\n", "")
    email_body = render_to_string("emails/contact/send_message_body.txt", c)

    email = EmailMessage(
        email_subject,
        email_body,
        email,
        [settings.DEFAULT_FROM_EMAIL],
        [],
        headers={"Reply-To": email},
    )
    return email.send(fail_silently=False)
