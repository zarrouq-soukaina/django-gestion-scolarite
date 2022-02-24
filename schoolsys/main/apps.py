from django.apps import AppConfig
from suit.apps import DjangoSuitConfig



class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    
    

class SuitConfig(DjangoSuitConfig):
    layout= 'vertical'