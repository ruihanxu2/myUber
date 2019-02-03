from django.apps import AppConfig


class UberConfig(AppConfig):
    name = 'uber'

    def ready(self):
        import uber.signals