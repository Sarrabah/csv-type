import requests


def is_csv(url: str) -> bool:
    head = requests.head(url)
    header = head.headers
    content_type = header["Content-type"]
    print(header)
    content_type_arr = content_type.split(";")
    if content_type_arr[0] == "text/csv":
        return True
    return False

#print(is_csv('https://data.opendatasoft.com/api/explore/v2.1/catalog/datasets/prenoms-des-enfants-nes-a-angers@angersloiremetropole/exports/csv'))