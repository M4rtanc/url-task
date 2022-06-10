import util_functions


def protect_uid_to_url(url: str, uid: str) -> str:
    """Returns url path with encoded uid."""
    if url[-1] != "/":  # assumes that url is not empty and valid
        url += "/"
    return url + util_functions.cipher_text(uid)


def get_uid_from_url(url: str) -> str:
    """Returns encoded uid from url."""
    return url.split("/")[-1]


def get_uid_from_url_decoded(url: str) -> str:
    """Returns decoded uid from url."""
    return util_functions.decipher_text(get_uid_from_url(url))
