import unittest

from models.sku import SKU
from libs.sku_manager import check_sku, generate_sku


class TestSKU(unittest.TestCase):
    def test_sku_representations(self):
        sku = SKU("123456789123")
        sku1 = SKU("123456789123")
        sku2 = SKU("111111111111")
        sku3 = SKU("1111")
        sku4 = SKU("11111111111111111111")

        self.assertEqual(sku, sku1)
        self.assertNotEqual(sku, sku2)
        self.assertRaises(ValueError, check_sku, sku3)
        self.assertRaises(ValueError, check_sku, sku4)

        self.assertEqual(sku[0], 1)
        self.assertEqual(sku[1], 2)
        self.assertEqual(sku[2], 3)
        self.assertEqual(sku[3], 4)
        self.assertEqual(sku[4], 5)
        self.assertEqual(sku[5], 6)
        self.assertEqual(sku[6], 7)
        self.assertEqual(sku[7], 8)
        self.assertEqual(sku[8], 9)
        self.assertEqual(sku[9], 1)
        self.assertEqual(sku[10], 2)
        self.assertEqual(sku[11], 3)

    def test_correct_sku(self):
        sku = SKU("515351525152")
        self.assertEqual(check_sku(sku), True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
