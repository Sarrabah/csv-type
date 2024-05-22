from url_content_type_services.url_content_type_services import IRequestService


def is_csv(url: str, requestService: IRequestService) -> bool:

    content_type = requestService.get_content_type_from_header(url)
    if content_type is None:
        return False

    content_type_arr = content_type.split(";")
    if content_type_arr[0] == "text/csv":
        return True

    return False
