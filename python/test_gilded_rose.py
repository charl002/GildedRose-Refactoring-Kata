# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_sell_date_quality_degrade(self):
        items = [Item("test1", -5, 10), Item("Sulfuras, Hand of Ragnaros", -5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        self.assertEqual(80, items[1].quality)

    def test_quality_is_never_negative(self):
        items = [Item("test1", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertNotEqual(-1, items[0].quality)

    def test_aged_brie_quality_increase(self):
        items = [Item("Aged Brie", 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_quality_never_more_than_50(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80), Item("Aged Brie", -5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertNotEqual(51, items[1].quality)
        self.assertEqual(80, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
