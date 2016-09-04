from game import Turnament
from player import Player

__author__ = 'Stian R. Hanssen'

HISTORIAN_QUESTION = "What is the memory span of the historian? "
OPTIONS = " [0: Random, 1: Sequential, 2: Most Common, 3: Historian] "


def run():
    hist_num1 = 0
    hist_num2 = 0
    player1 = custom_text_input("Player 1 type?" + OPTIONS, '0', '1', '2', '3')
    if player1 == '3':
        hist_num1 = custom_type_input(HISTORIAN_QUESTION, int)
    player2 = custom_text_input("Player 2 type?" + OPTIONS, '0', '1', '2', '3')
    if player2 == '3':
        hist_num2 = custom_type_input(HISTORIAN_QUESTION, int)
    num_games = custom_type_input("How many games? ", int)
    player1 = Player.get_player(int(player1), hist_num1)
    player2 = Player.get_player(int(player2), hist_num2)
    turnament = Turnament(player1, player2, num_games)
    turnament.execute_turnament()


def custom_text_input(question, *expected_inputs):
    assert(isinstance(question, str))
    for inputs in expected_inputs:
        assert(isinstance(inputs, str))
    while True:
        answer = input(question)
        if answer.lower() in expected_inputs:
            return answer
        if answer.lower() == "exit" or answer.lower() == "stop":
            exit()


def custom_type_input(question, expected_type):
    assert(isinstance(question, str))
    while True:
        answer = input(question)
        if answer.lower() == "exit" or answer.lower() == "stop":
            exit()
        try:
            return expected_type(answer)
        except:
            pass

if __name__ == '__main__':
    run()
    wait = input()
