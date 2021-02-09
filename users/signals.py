# we import post_save so it will fired when object(post) is saved
from django.db.models.signals import post_save

# it is the sender because it sends the signal
from django.contrib.auth.models import User

# we will create a receiver, a function, that get a signal and perform some task
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()



