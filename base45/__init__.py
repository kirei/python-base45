"""
Base45 Data Encoding as described in draft-faltstrom-base45-02
"""

from typing import Union

BASE45_CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"


def b45encode(buf: bytes) -> bytes:
    """Convert bytes to base45-encoded string"""
    res = ""
    buflen = len(buf)
    for i in range(0, buflen, 2):
        if buflen - i > 1:
            x = (buf[i] << 8) + buf[i + 1]
            e, x = divmod(x, 45 * 45)
            d, c = divmod(x, 45)
            res += BASE45_CHARSET[c] + BASE45_CHARSET[d] + BASE45_CHARSET[e]
        else:
            x = buf[i]
            d, c = divmod(x, 45)
            res += BASE45_CHARSET[c] + BASE45_CHARSET[d]
    return res.encode()


def b45decode(s: Union[bytes, str]) -> bytes:
    """Decode base45-encoded string to bytes"""
    res = []
    try:
        if isinstance(s, str):
            buf = [BASE45_CHARSET.index(c) for c in s]
        else:
            buf = [BASE45_CHARSET.index(c) for c in s.decode()]
        buflen = len(buf)
        for i in range(0, buflen, 3):
            x = buf[i] + buf[i + 1] * 45
            if buflen - i >= 3:
                x = buf[i] + buf[i + 1] * 45 + buf[i + 2] * 45 * 45
                res.extend(list(divmod(x, 256)))
            else:
                res.append(x)
        return bytes(res)
    except (ValueError, IndexError, AttributeError):
        raise ValueError("Invalid base45 string")
