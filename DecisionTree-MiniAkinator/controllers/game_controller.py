from controllers.tree_controller import TreeController
from views.game_view import GameView
import os

class GameController:
    def __init__(self):
        self.__game_view = GameView(self)
        self.__tree_controller = TreeController(self)

    
    def start(self):
        self.open_view()

    def open_view(self):
        switcher = {
            1: self.play,
            2: self.include_theme,
            3: self.show_tutorial,
            4: self.reset_themes,
            0: self.shutdown,
        }

        while True:
            switcher[int(self.__game_view.show_options())]()

    def play(self):
        pass

    def include_theme(self):
        self.__tree_controller.include_theme()
        

    def show_tutorial(self):
        self.__game_view.show_tutorial()

    def reset_themes(self):
        if self.__game_view.reset_warning():
            path = os.path.join(os.path.dirname(__file__), f'..\\save_data')
            for file in os.listdir(path):
                if file == "tree.pkl":
                    path_to_file = os.path.join(path, file)
                    os.remove(path_to_file)
    def shutdown(self):
        exit(0)
    