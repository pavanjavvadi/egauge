from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "wekeza_energy.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import wekeza_energy.users.signals  # noqa F401
        except ImportError:
            pass
