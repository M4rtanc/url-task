import base64
import random


def xor_chars(a: str, b: str) -> str:
    """XOR operation on two characters."""
    return chr(ord(a) ^ ord(b))


def xor_text(plain_text: str) -> str:
    """XOR with text and random character which is appended at the beginning."""
    rand_char = chr(random.randint(0, 128))  # characters defined in ascii
    result = rand_char
    for char in plain_text:
        result += (xor_chars(rand_char, char))
    return result


def de_xor_text(plain_text: str) -> str:
    """XOR with text and its first character."""
    rand_char = plain_text[0]
    result = ""
    for char in plain_text[1:]:
        result += xor_chars(rand_char, char)
    return result


def cipher_text(plain_text: str) -> str:
    """Ciphers text using XOR and Base64."""
    xored_text = xor_text(plain_text)
    xored_text_bytes = xored_text.encode("ascii")
    b64_bytes = base64.b64encode(xored_text_bytes)
    result = b64_bytes.decode("ascii")
    return result


def decipher_text(ciphered_text: str) -> str:
    """Deciphers text from Base64 and XOR."""
    b64_bytes = ciphered_text.encode("ascii")
    xored_text_bytes = base64.b64decode(b64_bytes)
    xored_text = xored_text_bytes.decode("ascii")
    result = de_xor_text(xored_text)
    return result


def tests():
    assert xor_chars(chr(11), chr(17)) == chr(26)
    assert xor_chars(chr(56), chr(3)) == chr(59)
    assert xor_chars(chr(112), chr(42)) == chr(90)
    assert xor_chars(chr(158), chr(31)) == chr(129)
    print("xor_chars OK")

    random.seed(5)  # rand_char = 'A'
    assert xor_text("Martin") == "A\x0c 35(/"
    random.seed(24)  # rand_char = 'b'
    assert xor_text("USERNAME") == "b71'0,#/'"
    random.seed(21)  # rand_char = '*'
    assert xor_text("abc42#?!") == "*KHI\x1e\x18\t\x15\x0b"
    random.seed(77)  # rand_char = '@'
    assert xor_text("pondeli") == "@0/.$%,)"
    print("xor_text OK")

    assert de_xor_text(xor_text("Martin")) == "Martin"
    assert de_xor_text(xor_text("USERNAME")) == "USERNAME"
    assert de_xor_text(xor_text("abc42#?!")) == "abc42#?!"
    assert de_xor_text(xor_text("pondeli")) == "pondeli"
    print("de_xor_text OK")

    random.seed(5)
    assert cipher_text("Martin") == "QQwgMzUoLw=="
    random.seed(24)
    assert cipher_text("USERNAME") == "YjcxJzAsIy8n"
    random.seed(21)
    assert cipher_text("abc42#?!") == "KktISR4YCRUL"
    random.seed(77)
    assert cipher_text("pondeli") == "QDAvLiQlLCk="
    print("cipher_text OK")

    assert decipher_text(cipher_text("Martin")) == "Martin"
    assert decipher_text(cipher_text("USERNAME")) == "USERNAME"
    assert decipher_text(cipher_text("abc42#?!")) == "abc42#?!"
    assert decipher_text(cipher_text("pondeli")) == "pondeli"
    print("decipher_text OK")
