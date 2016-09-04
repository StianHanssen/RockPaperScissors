from action import Action
from collections import Counter
from random import randint

__author__ = 'Stian R. Hanssen'


class Player:
    def __init__(self):
        self._history = []
        self.__points = 0

    def __str__(self):
        return self.__class__.__name__

    def recieve_result(self, action, point):
        self.__points += point
        self._history.append(action)

    def get_points(self):
        return self.__points

    def pick_action(self):
        raise NotImplementedError

    @staticmethod
    def get_player(num, historian_num):
        if num == 0:
            return RandomPlayer()
        elif num == 1:
            return SequentialPlayer()
        elif num == 2:
            return MostCommonPlayer()
        elif num == 3:
            return HistorianPlayer(historian_num)
        else:
            ValueError("No player by that number")


class RandomPlayer(Player):
    def pick_action(self):
        return Action(randint(0, 2))


class SequentialPlayer(Player):
    def __init__(self):
        super().__init__()
        self._prevMove = 2

    def pick_action(self):
        move = (self._prevMove + 1) % 3
        self._prevMove = move
        return Action(move)


class MostCommonPlayer(RandomPlayer):
    def pick_action(self):
        if not self._history:
            return super().pick_action()
        else:
            return Action.get_weakness(Counter(self._history).most_common(1)[0][0])


class HistorianPlayer(RandomPlayer):
    def __init__(self, memory):
        super().__init__()
        self.__memory = memory

    def __str__(self):
        return self.__class__.__name__ + "(" + str(self.__memory) + ")"

    def pick_action(self):
        if self._history:
            seq = self._history[-self.__memory:]
            occ = [0, 0, 0]
            for i in reversed(range(self.__memory - 1, len(self._history) - 1)):
                if self._history[i - self.__memory + 1:i + 1] == seq:
                    occ[self._history[i + 1].value] += 1
            if max(occ) > 0:
                return Action.get_weakness(occ.index(max(occ)))
        return super().pick_action()
