#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of mtgsdk.
# https://github.com/MagicTheGathering/mtg-sdk-python

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Andrew Backes <backes.andrew@gmail.com>

import asyncio
import unittest
from mtgsdk import Card


class TestCard(unittest.TestCase):
    def async_test(f):
        def wrapper(*args, **kwargs):
            coro = asyncio.coroutine(f)
            future = coro(*args, **kwargs)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(future)

        return wrapper

    def test_find_returns_card(self):
        card = yield from Card.find(88803)

        self.assertEqual('Choice of Damnations', card.name)
        self.assertEqual('{5}{B}', card.mana_cost)
        self.assertEqual(6, card.cmc)
        self.assertEqual('Sorcery — Arcane', card.type)
        self.assertTrue('Black' in card.colors)
        self.assertEqual(['B'], card.color_identity)
        self.assertTrue('Sorcery' in card.types)
        self.assertTrue('Arcane' in card.subtypes)
        self.assertEqual('Rare', card.rarity)
        self.assertEqual('SOK', card.set)
        self.assertEqual('Saviors of Kamigawa', card.set_name)
        self.assertEqual("Target opponent chooses a number. You may have that player lose that much life. If you don't, that player sacrifices all but that many permanents.", card.text)
        self.assertEqual("\"Life is a series of choices between bad and worse.\"\n—Toshiro Umezawa", card.flavor)
        self.assertEqual('Tim Hildebrandt', card.artist)
        self.assertEqual('62', card.number)
        self.assertEqual(88803, card.multiverse_id)
        self.assertEqual('http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=88803&type=card', card.image_url)
        self.assertTrue(len(card.rulings) > 0)
        self.assertTrue({"name":"Scelta della Dannazione","language":"Italian","multiverseid":105393, "imageUrl":"http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=105393&type=card"} in card.foreign_names)
        self.assertTrue('SOK' in card.printings)
        self.assertEqual("Target opponent chooses a number. You may have that player lose that much life. If you don't, that player sacrifices all but that many permanents.", card.original_text)
        self.assertEqual('Sorcery — Arcane', card.original_type)
        self.assertTrue({"format":"Commander","legality":"Legal"} in card.legalities)
        self.assertEqual('1c4aab072d52d283e902f2302afa255b39e0794b', card.id)

    def test_all_with_params_return_cards(self):
        cards = yield from Card.where(supertypes='legendary')
        cards = yield from cards.where(subtypes='elf,warrior')
        cards = yield from cards.all()

        self.assertTrue(len(cards) >= 13)

    def test_all_with_page_returns_cards(self):
        cards = yield from Card.where(page=1)
        cards = yield from cards.all()

        self.assertEqual(100, len(cards))

    def test_all_with_page_and_page_size_returns_card(self):
        cards = yield from Card.where(page=1)
        cards = yield from cards.where(pageSize=1)
        cards = yield from cards.all()

        self.assertEqual(1, len(cards))


