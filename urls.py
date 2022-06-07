from controllers.test import ping
from utils.url_manager import UrlManager


def load_endpoints(app):
    url_manager = UrlManager()

    url_manager.add_endpoint("/ping", "ping", ping, methods=["GET"])

    url_manager.setup_endpoints(app)
