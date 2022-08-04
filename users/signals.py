from users.models import Profile, Parent, Professor, Student
from django.dispatch import receiver
from django.db.models.signals import post_save

# Will handle all profiles in the system


@receiver(post_save, sender=Student)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.save()


@receiver(post_save, sender=Student)
def save_student_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Parent)
def create_parent_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.save()


@receiver(post_save, sender=Parent)
def save_parent_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Professor)
def create_professor_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.set_password('123456')
        instance.save()


@receiver(post_save, sender=Professor)
def save_professor_profile(sender, instance, **kwargs):
    instance.profile.save()
