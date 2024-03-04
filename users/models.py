from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verify_email = models.BooleanField(default=False)


#1m6|??XEg%
class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    expiration = models.DateTimeField()

    def __str__(self):
        return f"EmailVerification obj for {self.user.email}"

    def send_verification_email(self):
        link = reverse('users:email_verification', kwargs={'email': self.user.email, 'code': self.code})
        v_link = f'{settings.DOMAIN_NAME}{link}'
        send_mail(
            subject="Подтверждение электронной почты сервис Каршеринга",
            message="для подтверждения перейдите по ссылке {}".format(
                v_link
            ),
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

