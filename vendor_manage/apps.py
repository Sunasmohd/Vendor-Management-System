from django.apps import AppConfig


class VendorManageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vendor_manage'

    def ready(self) -> None:
        import vendor_manage.signals