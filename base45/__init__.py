"""
Base45 Data Encoding as described in draft-faltstrom-base45-02
"""

BASE45_CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"


def b45encode(s: bytes) -> str:
    """Convert bytes to base45-encoded string"""
    res = ""
    buf = list(s)
    while buf:
        if len(buf) >= 2:
            x = (buf.pop(0) << 8) + buf.pop(0)
            e = x // 45 // 45
            x -= e * 45 * 45
            d = x // 45
            c = x % 45
            res += BASE45_CHARSET[c] + BASE45_CHARSET[d] + BASE45_CHARSET[e]
        else:
            x = buf.pop(0)
            d = x // 45
            c = x % 45
            res += BASE45_CHARSET[c] + BASE45_CHARSET[d]
    return res


def b45decode(s: str) -> bytes:
    """Decode base45-encoded string to bytes"""
    res = []
    try:
        buf = [BASE45_CHARSET.index(c) for c in s]
        while buf:
            if len(buf) >= 3:
                x = buf.pop(0) + buf.pop(0) * 45 + buf.pop(0) * 45 * 45
                res.extend([x // 256, x % 256])
            else:
                x = buf.pop(0) + buf.pop(0) * 45
                res.extend([x % 256])
        return bytes(res)
    except (ValueError, IndexError):
        raise ValueError("Invalid base45 string")
