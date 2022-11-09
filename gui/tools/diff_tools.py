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
