# from django.core.cache import cache
# from django.db.models.signals import post_delete, post_save
# from .models import Category
# from django.dispatch import receiver


# @receiver(post_delete, sender=Category)
# def object_category_delete_handler(sender, **kwargs):
#      cache.delete('objects')


# @receiver(post_save, sender=Category)
# def object_category_save_handler(sender, **kwargs):
#     cache.delete('objects')


# from django.dispatch import receiver
# from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
 
 
# @receiver(user_logged_in)
# def log_user_login(sender, request, user, **kwargs):
#     print('user logged in')
 
 
# @receiver(user_login_failed)
# def log_user_login_failed(sender, credentials, request, **kwargs):
#     print('user logged in failed')
 
 
# @receiver(user_logged_out)
# def log_user_logout(sender, request, user, **kwargs):
#     print('user logged out')

from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    print('user {} logged in through page {}'.format(user.username, request.META.get('HTTP_REFERER')))


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    print('user {} logged in failed through page {}'.format(credentials.get('username'), request.META.get('HTTP_REFERER')))


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    print('user {} logged out through page {}'.format(user.username, request.META.get('HTTP_REFERER')))