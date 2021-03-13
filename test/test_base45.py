import unittest

from base45 import b45decode, b45encode

GOOD_DATA = [
    (b"AB", "BB8"),
    (b"Hello!!", "%69 VD92EX0"),
    (b"base-45", "UJCLQE7W581"),
    (b"ietf!", "QED8WEX0"),
    (
        b"The quick brown fox jumps over the lazy dog",
        "8UADZCKFEOEDJOD2KC54EM-DX.CH8FSKDQ$D.OE44E5$CS44+8DK44OEC3EFGVCD2",
    ),
]

BAD_STRINGS = ["xyzzy", "::::"]


class TestBase45(unittest.TestCase):
    def test_encode_simple(self):
        for binary_ref, encoded_ref in GOOD_DATA:
            encoded_res = b45encode(binary_ref)
            self.assertEqual(encoded_res, encoded_ref)

    def test_decode_simple(self):
        for binary_ref, encoded_ref in GOOD_DATA:
            binary_res = b45decode(encoded_ref)
            self.assertEqual(binary_res, binary_ref)

    def test_decode_bad(self):
        for v in BAD_STRINGS:
            with self.assertRaises(ValueError):
                b45decode(v)


if __name__ == "__main__":
    unittest.main()
