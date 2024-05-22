from abc import ABC
from typing import Optional
import requests


class IRequestService(ABC):
    def get_content_type_from_header(self, url: str) -> Optional[str]:
        ...


class RequestService(IRequestService):

    def get_content_type_from_url_header(self, url: str) -> Optional[str]:
        head = requests.head(url)
        header = head.headers
        if "Content-Type" in header:
            return header["Content-Type"]
        return None
