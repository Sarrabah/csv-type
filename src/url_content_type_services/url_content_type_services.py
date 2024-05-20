from abc import ABC, abstractmethod
import requests


class ContentTypeReaderServiceInterface(ABC):
    @abstractmethod
    def get_content_type_from_url_header(self, url: str) -> str:
        ...


class ContentTypeReaderService(ContentTypeReaderServiceInterface):
  
    def get_content_type_from_url_header(self, url: str) -> str:
        head = requests.head(url)
        header = head.headers
        content_type = header["Content-type"]
        return content_type
