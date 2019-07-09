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
    TWO = (2, '2')
    THREE = (3, '3')
    FOUR = (4, '4')
    FIVE = (5, '5')
    SIX = (6, '6')
    QUEEN = (7, 'Q')
    JACK = (8, 'J')
    KING = (9, 'K')
    SEVEN = (10, '7')
    ACE = (11, 'A')

    def __int__(self):
        return self[0]

    def __str__(self):
        return self[1]

    def __lt__(self, other):
        return int(self) < int(other)

    def __le__(self, other):
        return int(self) <= int(other)

    def __eq__(self, other):
        return int(self) == int(other)

    def __ge__(self, other):
        return int(self) >= int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __ne__(self, other):
        return int(self) != int(other)


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


class EmptyDeckError(Exception):
    pass


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]

        self.shuffle()

    def shuffle(self):
        np.random.shuffle(self.cards)

    def draw(self):
        try:
            return self.cards.pop()
        except IndexError:
            raise EmptyDeckError


class BiscolaSelfPlayEnv(gym.Env):
    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        pass
