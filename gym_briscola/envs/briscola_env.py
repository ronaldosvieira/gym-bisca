# -*- coding: utf-8 -*-

import gym
import numpy as np

from enum import Enum


class Suit(Enum):
    HEARTS = '♥'
    DIAMONDS = '♦'
    CLUBS = '♣'
    SPADES = '♠'


class Rank(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    JACK = 8
    QUEEN = 9
    KING = 10
    ACE = 11


class BiscolaEnv(gym.Env):
    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        pass
