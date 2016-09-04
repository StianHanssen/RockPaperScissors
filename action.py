from enum import Enum

__author__ = 'Stian R. Hanssen'


class Action(Enum):
    Rock = 0
    Paper = 1
    Scissor = 2

    def __gt__(self, other):
        return Action.get_weakness(other) == self

    def __str__(self):
        return self.name

    @staticmethod
    def get_weakness(action):
        return Action((Action(action).value + 1) % 3)
