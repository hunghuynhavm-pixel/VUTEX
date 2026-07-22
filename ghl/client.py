"""Client gọi GHL API 2.0 (LeadConnector)."""
import requests

from .config import Config


class GHLClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {Config.TOKEN}",
            "Version": Config.API_VERSION,
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    def _url(self, path):
        return Config.BASE_URL + path

    def get(self, path, params=None):
        r = self.session.get(self._url(path), params=params, timeout=30)
        return self._handle(r)

    def post(self, path, json=None):
        r = self.session.post(self._url(path), json=json, timeout=30)
        return self._handle(r)

    @staticmethod
    def _handle(r):
        if r.status_code >= 400:
            raise RuntimeError(
                f"GHL API lỗi {r.status_code}: {r.text[:500]}"
            )
        if not r.text:
            return {}
        return r.json()
