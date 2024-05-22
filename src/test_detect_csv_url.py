from typing import Type
from detect_csv_url import is_csv
from url_content_type_services.url_content_type_services import IRequestService


def make_test_class(content_type: str) -> Type[IRequestService]:

    class TestTypeReaderService(IRequestService):
        def get_content_type_from_header(self, url: str) -> str:
            return content_type

    return TestTypeReaderService


TestCsvRequestService = make_test_class("text/csv; charset=utf-8")
TestNotCsvRequestService = make_test_class("pplication/octet-stream")
TestVoidRequestService = make_test_class("")


def test_csv_url_content_type():
    all_content_type = TestCsvRequestService()
    assert is_csv("https://fakedata.opendatasoft.com/apii/explore/v2.1/catalog/datasets/prenoms-des-enfants-nes-a-angers@angersloiremetropole/exports/csv", all_content_type) is True


def test_not_csv_url_content_type():
    all_content_type = TestNotCsvRequestService()
    assert is_csv("https://fakegitlab.com/validata-table/validata-table/uploads/f0091cba92766b0015fb0015e8c594fc/prenoms-des-enfants-nes-a-angers_angersloiremetropole.csv", all_content_type) is False


def test_void_url_content_type():
    all_content_type = TestVoidRequestService()
    assert is_csv("https://fakedata.opendatasoft.com/apii/explore/v2.1/catalog/datasets/prenoms-des-enfants-nes-a-angers@angersloiremetropole/exports/csv", all_content_type) is False
