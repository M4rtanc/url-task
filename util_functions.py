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
