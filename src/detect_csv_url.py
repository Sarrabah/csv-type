from url_content_type_services.url_content_type_services import ContentTypeReaderServiceInterface


class CsvDective:
    def __init__(self, content_type: ContentTypeReaderServiceInterface):
        self.content_type = content_type
    
    def is_csv(self, url: str) -> bool:
        content_type = self.content_type.get_content_type_from_url_header(url)
        content_type_arr = content_type.split(";")
        if content_type_arr[0] == "text/csv":
            return True
        return False
