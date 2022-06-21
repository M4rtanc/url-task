import util_functions
import random
from typing import Optional


def protect_uid_to_url(url: str, arg_name: str, uid: str) -> str:
    """Returns url path with encoded uid."""
    return url + "?" + arg_name + "=" + util_functions.cipher_text(uid)


def get_arg_from_url(url: str, arg_name: str) -> Optional[str]:
    """Returns encoded uid from url."""
    if "?" + arg_name + "=" not in url:
        return None
    return url.split("?" + arg_name + "=")[-1]


def get_uid_from_url_decoded(url: str, arg_name: str) -> str:
    """Returns decoded uid from url."""
    encoded_uid = get_arg_from_url(url, arg_name)
    if not encoded_uid:
        return encoded_uid
    return util_functions.decipher_text(encoded_uid)


def tests():
    random.seed(5)
    assert protect_uid_to_url("https://email.seznam.cz/login", "user", "Martin") == "https://email.seznam.cz/login?user=QQwgMzUoLw=="
    random.seed(24)
    assert protect_uid_to_url("https://www.messenger.com/t", "id","USERNAME") == "https://www.messenger.com/t?id=YjcxJzAsIy8n"
    random.seed(21)
    assert protect_uid_to_url("https://osel.cz/16564", "title", "abc42#?!") == "https://osel.cz/16564?title=KktISR4YCRUL"
    random.seed(77)
    assert protect_uid_to_url("https://www.novinky.cz/cestovani", "category","pondeli") == "https://www.novinky.cz/cestovani?category=QDAvLiQlLCk="
    print("protect_uid_to_url OK")

    assert get_arg_from_url("https://email.seznam.cz/login?user=QQwgMzUoLw==", "user") == "QQwgMzUoLw=="
    assert get_arg_from_url("https://www.messenger.com/t?id=YjcxJzAsIy8n", "id") == "YjcxJzAsIy8n"
    assert get_arg_from_url("https://www.messenger.com/t?id=YjcxJzAsIy8n", "ID") is None
    assert get_arg_from_url("https://osel.cz/16564?title=KktISR4YCRUL", "title") == "KktISR4YCRUL"
    assert get_arg_from_url("https://www.novinky.cz/cestovani?category=QDAvLiQlLCk=", "category") == "QDAvLiQlLCk="
    assert get_arg_from_url("https://www.novinky.cz/cestovani?category=QDAvLiQlLCk=", "categ") is None
    print("get_arg_from_url OK")

    assert get_uid_from_url_decoded("https://email.seznam.cz/login?user=QQwgMzUoLw==", "user") == "Martin"
    assert get_uid_from_url_decoded("https://www.messenger.com/t?id=YjcxJzAsIy8n", "id") == "USERNAME"
    assert get_uid_from_url_decoded("https://osel.cz/16564?title=KktISR4YCRUL", "title") == "abc42#?!"
    assert get_uid_from_url_decoded("https://www.novinky.cz/cestovani?category=QDAvLiQlLCk=", "category") == "pondeli"
    print("get_uid_from_url_decoded OK")
