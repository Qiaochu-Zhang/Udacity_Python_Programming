#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RockPlayer(Player):
    pass

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.num = 0

    def move(self):
        if self.num == 0:
            self.first = random.choice(moves)
            self.num += 1
            return self.first
        else:
            return self.next

    def learn(self, my_move, their_move):
        if my_move == 'rock':
            self.next = 'paper'
        elif my_move == 'paper':
            self.next = 'scissors'
        else:
            self.next = 'rock'


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.num = 0

    def move(self):
        if self.num == 0:
            self.first = random.choice(moves)
            self.num += 1
            return self.first
        else:
            return self.next

    def learn(self, my_move, their_move):
        self.next = their_move


class HumanPlayer(Player):
    def move(self):
        self.choice = input("Rock, paper, scissors? ").lower()
        if self.choice not in ['rock', 'paper', 'scissors']:
            self.choice = HumanPlayer.move(self)
        return self.choice


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You: {move1}  Computer Player : {move2}")
        if beats(move1, move2):
            self.p1.score += 1
            print('You win')
        elif beats(move2, move1):
            self.p2.score += 1
            print('Computer Player wins')
        else:
            print('**Tie**')
        print("Score: Player One " + str(self.p1.score) +
              ", Player Two " + str(self.p2.score))
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        self.round = 0
        while "quit" != input('type "quit" to quit,'
                              ' others to continue.').lower():
            print(f"Round {self.round}:")
            self.round += 1
            self.play_round()
        print("Game over!")
        if self.p1.score > self.p2.score:
            print('You win!')
        elif self.p1.score < self.p2.score:
            print('Computer Player wins')
        else:
            print('**Tie**')
        print("Final scores: You "+str(self.p1.score) +
              ", Computer Player "+str(self.p2.score) + '.')


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
