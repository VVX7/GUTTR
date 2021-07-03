import os
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class TimeoutHTTPAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.timeout = 3
        if kwargs.get("timeout"):
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None:
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


def client():
    # Handles rate limit by reading 429 status code in HTTP header.
    retry_strategy = Retry(
        total=7,
        # Use incremental backoff.
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        method_whitelist=["GET", "PATCH"]
    )
    adapter = TimeoutHTTPAdapter(timeout=2, max_retries=retry_strategy)
    session = requests.Session()
    session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
    session.headers["x-app-auth"] = str({"user": os.environ["user"], "token": os.environ["jwt"]})
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    return session