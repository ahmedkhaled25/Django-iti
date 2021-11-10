from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Movie

@receiver(post_save, sender=Movie)
def my_handler(sender, instance, created, *args, **kwargs):
    send_mail(
              subject='New Movie created',
              message='Dear user {} has been created'.format(instance.name),
              from_email = 'notifiersys@gmail.com',
              recipient_list = ['receivers-1', 'receiver-2'],
              fail_silently = False
              )
