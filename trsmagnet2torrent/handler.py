import base64
import logging

import requests
from asgiref.sync import async_to_sync
from magnet2torrent import FailedToFetchException, Magnet2Torrent
from tridentstream.plugins import MagnetResolverPlugin
from unplugged import Schema, fields

logger = logging.getLogger(__name__)


class Magnet2TorrentMagnetResolverSchema(Schema):
    url = fields.String(
        required=False, ui_schema={"ui:title": "External Magnet2Torrent URL"}
    )
    use_external_server = fields.Boolean(default=False, title="Use External Server")


class Magnet2TorrentMagnetResolverPlugin(MagnetResolverPlugin):
    plugin_name = "magnet2torrent"
    config_schema = Magnet2TorrentMagnetResolverSchema
    simpleadmin_templates = True

    def magnet_to_torrent(self, magnet_link):
        if self.config["use_external_server"]:
            r = requests.get(self.config["url"], params={"magnet": magnet_link})
            if not r.status_code == 200:
                return None

            return base64.b64decode(r.json()["torrent_data"])
        else:
            m2t = Magnet2Torrent(magnet_link)
            try:
                filename, torrent_data = async_to_sync(m2t.retrieve_torrent)()
            except FailedToFetchException:
                logger.exception("Failed to retrieve magnet link")
                return None

            return torrent_data
