from string import digits, ascii_letters
from gui.tools.exceptions import *

CHARS = digits + ascii_letters


def encrypt(s, step):
    res = ''
    for c in s:
        res += chr(ord(c) + step)
    return res


def decrypt(s, step):
    res = ''
    for c in s:
        res += chr(ord(c) - step)
    return res


def passwd_check(passwd):
    assert isinstance(passwd, str)
    if len(passwd) < 8:
        raise TooShort
    if not all(c in CHARS for c in passwd):
        raise IncorrectChars
    if not any(c in ascii_letters for c in passwd):
        raise NoASCII
    if all(c.isupper() for c in passwd if c.isascii()):
        raise OnlyUpper
    if all(c.islower() for c in passwd if c.isascii()):
        raise OnlyLower
    if not any(c.isdigit() for c in passwd):
        raise NoDigits
    return True
