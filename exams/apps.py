from django.apps import AppConfig


# Link to explain where signal handlers should be put 
# https://stackoverflow.com/questions/2719038/where-should-signal-handlers-live-in-a-django-project#:~:text=If%20you're%20using%20the,happened%20in%20the%20models%20module.
'''
Best practice is to define your handlers in handlers.py in a signals submodule, e.g. a file that looks like:

yourapp/signals/handlers.py:

from django.db.models.signals import pre_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(pre_save, sender=MyModel)
def my_handler(sender, **kwargs):
    pass
The best place to register your signal handler is then in the AppConfig of the app that defines it, using the ready() method. This will look like this:

yourapp/apps.py:

from django.apps import AppConfig

class TasksConfig(AppConfig):
    name = 'tasks'
    verbose_name = "Tasks"

    def ready(self):
        import yourproject.yourapp.signals.handlers #noqa
Make sure you're loading your AppConfig by specifying it either directly in your settings.py's INSTALLED_APPS, or in the __init__ of your app. See see the ready() documentation for more information.



'''

class ExamsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exams'
    verbose_name = "exams"
    
    def ready(self):
        import exams.signals
