import pytest
from detect_csv_url import CsvDective
from url_content_type_services.url_content_type_services import ContentTypeReaderServiceInterface


class TestCsvContentTypeReaderService(ContentTypeReaderServiceInterface):
    def get_content_type_from_url_header(self, url: str) -> str:
        content_type = "text/csv; charset=utf-8"
        return content_type


class TestNotCsvContentTypeReaderService(ContentTypeReaderServiceInterface):
    def get_content_type_from_url_header(self, url: str) -> str:
        content_type = "application/octet-stream"
        return content_type


def test_csv_url_content_type():
    all_content_type = TestCsvContentTypeReaderService()
    content_type = CsvDective(all_content_type)
    assert content_type.is_csv("https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/prenoms-des-enfants-nes-a-angers@angersloiremetropole/exports/csv") is True


def test_not_csv_url_content_type():
    all_content_type = TestNotCsvContentTypeReaderService()
    content_type = CsvDective(all_content_type)
    assert content_type.is_csv("https://gitlab.com/validata-table/validata-table/uploads/f0091cba92766b0015fb0015e8c594fc/prenoms-des-enfants-nes-a-angers_angersloiremetropole.csv") is False