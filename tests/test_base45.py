import random
import unittest

from base45 import b45decode, b45encode

GOOD_DATA = [
    (b"", b""),
    (b"\x00", b"00"),
    (b"\x01", b"10"),
    (b"\x2c", b":0"),
    (b"\x2d", b"01"),
    (b"\x07\xe8", b"::0"),
    (b"AB", b"BB8"),
    (b"\xff\xff", b"FGW"),
    (b"Hello!!", b"%69 VD92EX0"),
    (b"base-45", b"UJCLQE7W581"),
    (b"ietf!", b"QED8WEX0"),
    (b"\x0d\x0e\x0a\x0d\x0c\x00\x0f\x0f\x0e\x21", b"CT18C1CN1U+1HZ1"),
    (b"\x00\x00\x00\x00\x00\x00\x00\x00", b"000000000000"),
    (b"\x00\x00\x00\x00\x00\x00\x00", b"00000000000"),
    (
        b"The quick brown fox jumps over the lazy dog",
        b"8UADZCKFEOEDJOD2KC54EM-DX.CH8FSKDQ$D.OE44E5$CS44+8DK44OEC3EFGVCD2",
    ),
    (bytes("foo © bar 𝌆 baz", "UTF-8"), b"X.C82EIROA44GECH74C-J1/GUJCW2"),
]

BAD_BASE45_STRINGS = [b"xyzzy", b"::::", b"a", b"GGW", b":", b"0", b"::"]


class TestBase45(unittest.TestCase):
    def test_encode_good(self):
        for binary_ref, encoded_ref in GOOD_DATA:
            encoded_res = b45encode(binary_ref)
            self.assertEqual(encoded_res, encoded_ref)

    def test_decode_good(self):
        for binary_ref, encoded_ref in GOOD_DATA:
            binary_res = b45decode(encoded_ref)
            self.assertEqual(binary_res, binary_ref)

    def test_encode_bad(self):
        with self.assertRaises(TypeError):
            b45encode(42)

    def test_decode_bad(self):
        with self.assertRaises(TypeError):
            b45decode(42)
        for v in BAD_BASE45_STRINGS:
            with self.assertRaises(ValueError):
                b45decode(v)

    def test_decode_encoded(self):
        random.seed(42)
        for _ in range(142):
            binary = bytes(
                [random.randint(0, 255) for _ in range(random.randint(0, 142))]
            )
            self.assertEqual(binary, b45decode(b45encode(binary)))


if __name__ == "__main__":
    unittest.main()
