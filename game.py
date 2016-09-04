from action import Action

__author__ = 'Stian R. Hanssen'


class SingleGame():
    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2
        self.__point1 = 0
        self.__point2 = 0
        self.__pick1 = None
        self.__pick2 = None

    def execute_game(self):
        self.__pick1 = self.__player1.pick_action()
        self.__pick2 = self.__player2.pick_action()
        self.__point1 = 1 if self.__pick1 > self.__pick2 else (1/2 if self.__pick1 == self.__pick2 else 0)
        self.__point2 = 1 if self.__pick1 < self.__pick2 else (1/2 if self.__pick1 == self.__pick2 else 0)
        self.__player1.recieve_result(self.__pick2, self.__point1)
        self.__player2.recieve_result(self.__pick1, self.__point2)

    def __str__(self):
        if self.__pick1 is None and self.__pick2 is None:
            return "Game has not been executed"
        res = self.__point1 - self.__point2
        winner = "No one" if res == 0 else (self.__player1 if res > 0 else self.__player2)
        feedback = "[" + str(self.__player1) + ": " + str(self.__pick1) + "] VS ["
        feedback += str(self.__player2) + ": " + str(self.__pick2)
        feedback += "] -> " + str(winner) + " won!"
        return feedback


class Turnament():
    def __init__(self, player1, player2, num_games):
        self.__player1 = player1
        self.__player2 = player2
        self.__num_games = num_games
        self.__single_game = SingleGame(player1, player2)

    def execute__single_game(self):
        self.__single_game.execute_game()
        print(self.__single_game)

    def execute_turnament(self):
        for i in range(self.__num_games):
            self.execute__single_game()
        total_points = self.__player1.get_points() + self.__player2.get_points()
        print(self.__player1, "got", str(100 * self.__player1.get_points() / total_points) + "% of the points")
        print(self.__player2, "got", str(100 * self.__player2.get_points() / total_points) + "% of the points")
