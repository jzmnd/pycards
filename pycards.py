#! /usr/bin/env python
"""
pycards.py
Class for a standard deck of cards

Created by Jeremy Smith on 2017-03-10
j.smith.03@cantab.net
"""

import os
import sys
import random

__author__ = "Jeremy Smith"
__version__ = "1.0"


CARD_DICT = {'Ac':"Ace of clubs", '2c':"Two of clubs", '3c':"Three of clubs", '4c':"Four of clubs",
             '5c':"Five of clubs", '6c':"Six of clubs", '7c':"Seven of clubs", '8c':"Eight of clubs", '9c':"Nine of clubs",
             'Tc':"Ten of clubs", 'Jc':"Jack of clubs", 'Qc':"Queen of clubs", 'Kc':"King of clubs",
             'Ad':"Ace of diamonds", '2d':"Two of diamonds", '3d':"Three of diamonds", '4d':"Four of diamonds",
             '5d':"Five of diamonds", '6d':"Six of diamonds", '7d':"Seven of diamonds", '8d':"Eight of diamonds", '9d':"Nine of diamonds",
             'Td':"Ten of diamonds", 'Jd':"Jack of diamonds", 'Qd':"Queen of diamonds", 'Kd':"King of diamonds",
             'Ah':"Ace of hearts", '2h':"Two of hearts", '3h':"Three of hearts", '4h':"Four of hearts",
             '5h':"Five of hearts", '6h':"Six of hearts", '7h':"Seven of hearts", '8h':"Eight of hearts", '9h':"Nine of hearts",
             'Th':"Ten of hearts", 'Jh':"Jack of hearts", 'Qh':"Queen of hearts", 'Kh':"King of hearts",
             'As':"Ace of spades", '2s':"Two of spades", '3s':"Three of spades", '4s':"Four of spades",
             '5s':"Five of spades", '6s':"Six of spades", '7s':"Seven of spades", '8s':"Eight of spades", '9s':"Nine of spades",
             'Ts':"Ten of spades", 'Js':"Jack of spades", 'Qs':"Queen of spades", 'Ks':"King of spades",
             'jR':"Red joker", 'jB':"Black joker"}

RANK_DICT = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'j':None}


class Card():
    """Class for a single card"""
    def __init__(self, cid):
        self.cid = cid
        self.name = CARD_DICT[cid]
        self.rank = cid[0]
        self.suit = cid[1]
        self.ranknum = RANK_DICT[self.rank]

    def __repr__(self):
        return self.cid

    def black(self):
        return self.suit is 'c' or self.suit is 's' or self.suit is 'B'

    def face(self):
        return self.rank is 'J' or self.rank is 'Q' or self.rank is 'K'

    def joker(self):
        return self.rank is 'j'


class Deck():
    """Class for single deck of cards"""
    def __init__(self, include_jokers=True):
        self._suits = ['c', 'd', 'h', 's']
        self._ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

        self.drawList = [Card(r + s) for s in self._suits for r in self._ranks]
        self.discardList = []

        if include_jokers:
            self.drawList.append(Card('jR'))
            self.drawList.append(Card('jB'))

    def __getitem__(self, i):
        return self.drawList[i]

    def draw(self, n):
        clist = []
        if len(self.drawList) < n:
            return clist
        for i in xrange(n):
            c = self.drawList.pop(0)
            self.discardList.append(c)
            clist.append(c)
        return clist

    def cut(self):
        return random.choice(self.drawList)

    def topcard(self):
        return self.drawList[0]

    def shuffle(self):
        random.shuffle(self.drawList)
        return

    def shuffle_discard(self):
        random.shuffle(self.discardList)
        return

    def drawsize(self):
        return len(self.drawList)

    def discardsize(self):
        return len(self.discardList)

    def reset(self):
        self.drawList += self.discardList
        self.discardList = []
        return
