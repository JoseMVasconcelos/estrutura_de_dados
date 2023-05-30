from models.decision_tree import DecisionTree
from controllers.game_controller import GameController


class TreeController():
    def __init__(self, game_controller):
        self.__game_controller = game_controller