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
    ACE = 'A'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'


class Deck:
    def __init__(self):
        self.cards = [(suit, rank) for suit in Suit for rank in Rank]

        self.shuffle()

    def shuffle(self):
        np.random.shuffle(self.cards)

    def draw(self, amount=1):
        return self.cards.pop(amount)


class BiscolaSelfPlayEnv(gym.Env):
    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        pass
