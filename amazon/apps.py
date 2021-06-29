from django.apps import AppConfig


class AmazonConfig(AppConfig):
    name = 'amazon'
    
    # def ready(self):
    #     from .Scheduler import scheduler
    #     if settings.SCHEDULER_AUTOSTART:
    #         scheduler.start()