from django.apps import AppConfig


'''
The AppConfig class is used to define the configuration of the application.
It includes attributes such as name, verbose_name, default_auto_field, label, ready(), create_permissions(), etc.
The apps.py file contains a class, in this case 'ExamsConfig' that extends the AppConfig class from the django.apps module.
'''
class ExamsConfig(AppConfig): 
    
    # provides a default value for the AutoField used for primary keys in models.BigAutoField is 64-bit based and provides a wider range for pk
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exams'
    verbose_name = "exams"
    
    # Sets up signal handlers needed to be registered in the application when it starts. 
    def ready(self):
        import api.signals
        
  
        
        
