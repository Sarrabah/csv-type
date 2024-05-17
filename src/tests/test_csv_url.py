from csvtype import detect_csv_url


def test_csv_url():
    # l'inversion de dépendances ??
    assert detect_csv_url.is_csv("https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/prenoms-des-enfants-nes-a-angers@angersloiremetropole/exports/csv") is True   
   
    # normalement c'est un url de type csv mais son content-type est égale à 'application/octet-stream' (à voir)
    assert detect_csv_url.is_csv("https://gitlab.com/validata-table/validata-table/uploads/f0091cba92766b0015fb0015e8c594fc/prenoms-des-enfants-nes-a-angers_angersloiremetropole.csv") is True
