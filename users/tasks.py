from celery import shared_task
from datetime import timedelta
from django.utils.timezone import now
from users.models import User, EmailVerification
import uuid


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    exp = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=exp)
    record.send_verification_email()