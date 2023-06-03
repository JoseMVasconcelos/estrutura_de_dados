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
            1: self.get_tree_play,
            2: self.include_theme,
            3: self.show_tutorial,
            4: self.reset_themes,
            0: self.shutdown,
        }

        while True:
            switcher[int(self.__game_view.show_options())]()

    def play(self, node):
        if not node.isleaf:
            if self.__game_view.game_screen(node):
                self.play(node.right)
            else:
                self.play(node.left)
        else:
            if self.__game_view.final_guess(node):
                self.__game_view.show_message("Acertei! Tente pensar em algo mais difícil!")
            else:
                self.__tree_controller.add_new_node(node)
                self.__game_view.show_message("Você venceu... Pense em outra coisa, dessa vez acertarei!")

    def get_tree_play(self):
        themes = self.__tree_controller.get_themes()
        if themes:
            chosen_theme = self.__game_view.choose_theme(themes)
            tree = self.__tree_controller.search_tree_by_theme(chosen_theme)
            self.play(tree.root)
            self.__tree_controller.update(tree)
        else:
            self.__game_view.show_message("É necessário incluir um tema primeiro!")
            self.include_theme()

    def include_theme(self):
        self.__tree_controller.include_theme()

    def show_tutorial(self):
        self.__game_view.show_tutorial()

    def reset_themes(self):
        if self.__game_view.reset_warning():
            self.__tree_controller.reset_themes()

    def shutdown(self):
        exit(0)
    