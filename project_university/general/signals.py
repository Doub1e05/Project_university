from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from .models import Works, Status, User
import random
from django.db import IntegrityError

@receiver(post_save, sender=Works)
def create_statuses(sender, instance, created, **kwargs):
    if created:
        thread = instance.thread
        users = User.objects.filter(thread=thread)
        for user in users:
            while True:
                identifier = random.randint(100000, 999999)
                try:
                    Status.objects.create(work=instance, student=user, status='', identifier=identifier)
                    break
                except IntegrityError:
                    continue

@receiver(pre_save, sender=User)
def validate_user_thread(sender, instance, **kwargs):
    instance.full_clean()

@receiver(post_delete, sender=Status)
def delete_works_if_no_statuses(sender, instance, **kwargs):
    work_id = instance.work_id

    has_statuses = Status.objects.filter(work_id=work_id).exists()

    if not has_statuses:
        Works.objects.filter(pk=work_id).delete()