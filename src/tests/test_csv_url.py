import pytest
from csvtype import detect_csv_url


def test_csv_url():
    assert detect_csv_url.is_csv("https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/prenoms-des-enfants-nes-a-angers@angersloiremetropole/exports/csv") == True
    assert detect_csv_url.is_csv("https://gitlab.com/validata-table/validata-table/uploads/f0091cba92766b0015fb0015e8c594fc/prenoms-des-enfants-nes-a-angers_angersloiremetropole.csv") == True
