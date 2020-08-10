from django.apps import AppConfig


class App3Config(AppConfig):
    name = 'app3'

    def ready(self):
        import app3.signals
