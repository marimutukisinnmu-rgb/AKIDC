import unittest

from main import parse_target


class ParseTargetTests(unittest.TestCase):
    def test_plain_number(self):
        self.assertEqual(parse_target("200"), 200)

    def test_quoted_anka_syntax(self):
        self.assertEqual(parse_target(">>222"), 222)

    def test_rejects_zero(self):
        with self.assertRaises(Exception):
            parse_target("0")

    def test_rejects_non_number(self):
        with self.assertRaises(Exception):
            parse_target("abc")


if __name__ == "__main__":
    unittest.main()
