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


class Deck:
    def __init__(self):
        self.cards = [(suit, rank) for suit in Suit for rank in Rank]

        self.shuffle()

    def shuffle(self):
        np.random.shuffle(self.cards)

    def draw(self, amount=1):
        return self.cards.pop(amount)


class BiscolaEnv(gym.Env):
    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        pass
