from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = "magnet2torrent"
    verbose_name = "Magnet2Torrent MagnetResolver"
    label = "magnetresolver_magnet2torrent"

    def ready(self):
        from .handler import Magnet2TorrentMagnetResolverPlugin
