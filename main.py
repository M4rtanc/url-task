import util_functions
import random


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


def tests():
    random.seed(5)
    assert protect_uid_to_url("https://email.seznam.cz/", "Martin") == "https://email.seznam.cz/QQwgMzUoLw=="
    random.seed(24)
    assert protect_uid_to_url("https://www.messenger.com/t", "USERNAME") == "https://www.messenger.com/t/YjcxJzAsIy8n"
    random.seed(21)
    assert protect_uid_to_url("https://osel.cz/", "abc42#?!") == "https://osel.cz/KktISR4YCRUL"
    random.seed(77)
    assert protect_uid_to_url("https://www.novinky.cz/cestovani", "pondeli") == "https://www.novinky.cz/cestovani/QDAvLiQlLCk="
    print("protect_uid_to_url OK")

    assert get_uid_from_url("https://email.seznam.cz/QQwgMzUoLw==") == "QQwgMzUoLw=="
    assert get_uid_from_url("https://www.messenger.com/t/YjcxJzAsIy8n") == "YjcxJzAsIy8n"
    assert get_uid_from_url("https://osel.cz/KktISR4YCRUL") == "KktISR4YCRUL"
    assert get_uid_from_url("https://www.novinky.cz/cestovani/QDAvLiQlLCk=") == "QDAvLiQlLCk="
    print("get_uid_from_url OK")

    assert get_uid_from_url_decoded("https://email.seznam.cz/QQwgMzUoLw==") == "Martin"
    assert get_uid_from_url_decoded("https://www.messenger.com/t/YjcxJzAsIy8n") == "USERNAME"
    assert get_uid_from_url_decoded("https://osel.cz/KktISR4YCRUL") == "abc42#?!"
    assert get_uid_from_url_decoded("https://www.novinky.cz/cestovani/QDAvLiQlLCk=") == "pondeli"
    print("get_uid_from_url_decoded OK")
