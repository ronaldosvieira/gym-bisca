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
        return self.value[0]

    def __str__(self):
        return self.value[1]

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

    def __hash__(self):
        return int(self)


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


class Game:
    def __init__(self):
        self.players = 2
        self.scoring = {
            Rank.TWO: 0, Rank.THREE: 0, Rank.FOUR: 0, Rank.FIVE: 0,
            Rank.SIX: 0, Rank.QUEEN: 2, Rank.JACK: 3, Rank.KING: 4,
            Rank.SEVEN: 10, Rank.ACE: 11
        }

        self.deck = Deck()
        self.hands = tuple(list() for _ in range(self.players))
        self.points = [0 for _ in range(self.players)]
        self.board = [None for _ in range(self.players)]

        for hand in self.hands:
            for _ in range(3):
                hand.append(self.deck.draw())

        self.briscola = self.deck.draw()

        self.turn = 0
        self.lead_player = np.random.randint(self.players)
        self.active_player = 0

    def step(self, action):
        card = self.hands[self.active_player].pop(action)

        self.board[self.active_player] = card

        done = False

        if all([c is not None for c in self.board]):
            winner = self._get_winner()

            for card in self.board:
                self.points[winner] += self.scoring[card.rank]

            self.board = [None for _ in range(self.players)]

            try:
                new_cards = []

                for _ in range(self.players):
                    new_cards.append(self.deck.draw())

                for hand in self.hands:
                    hand.append(new_cards.pop())
            except EmptyDeckError:
                pass

            self.turn += 1
            self.lead_player = winner
            self.active_player = winner

            if len(self.hands[0]) == 0:
                done = True
        else:
            self.active_player = (self.active_player + 1) % self.players

        return done

    def _get_winner(self):
        lead_card = self.board[self.lead_player]

        briscolas = list(filter(
            lambda c: c[1].suit == self.briscola.suit,
            enumerate(self.board)))
        same_suit = list(filter(
            lambda c: c[1].suit == lead_card.suit,
            enumerate(self.board)))

        if len(briscolas) > 0:
            return max(briscolas, key=lambda c: c[1].rank)[0]
        elif len(same_suit) > 0:
            return max(same_suit, key=lambda c: c[1].rank)[0]
        else:
            return self.lead_player


class BiscolaSelfPlayEnv(gym.Env):
    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        pass
