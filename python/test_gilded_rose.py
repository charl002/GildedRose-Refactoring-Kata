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
    
    def test_sell_date_decrease(self):
        items = [Item("test1", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

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

    def test_sulfarus_date_never_drops(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertNotEqual(4, items[0].sell_in)
        self.assertEqual(5, items[0].sell_in)

    def test_conjured_item_value_decrease_by_two(self):
        items = [Item("Conjured Mana Cake", 5, 22), Item("Conjured Mana Cake", 5, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(20, items[0].quality)
        self.assertEqual(0, items[1].quality)

    def test_back_stage_pass_increase_value(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12, 20), Item("Backstage passes to a TAFKAL80ETC concert", 8, 20), Item("Backstage passes to a TAFKAL80ETC concert", 4, 20), Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(22, items[1].quality)
        self.assertEqual(23, items[2].quality)
        self.assertEqual(0, items[3].quality)


        
if __name__ == '__main__':
    unittest.main()
