#! /usr/bin/env python
"""
gravecardutils.py

Created by Jeremy Smith on 2017-03-10
j.smith.03@cantab.net
"""

import os
import sys
import random
from pycards import *

__author__ = "Jeremy Smith"
__version__ = "1.0"


def passtest(hand, target, statsuit='c', mod=0):
    p = False
    for c in hand:
        if c.joker():
            continue
        if c.ranknum <= target + mod:
            p = True
            continue
        if c.suit is statsuit and c.ranknum <= target + mod + 1:
            p = True
            continue
    return p


def facecardbonus(hand):
    bonus = 0
    for c in hand:
        if c.face():
            b = c.ranknum - 10
            if b > bonus:
                bonus = b
    return bonus


def jokercheck(hand):
    j = False
    for c in hand:
        if c.joker():
            j = True
    return j
