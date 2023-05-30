from controllers.tree_controller import TreeController


class GameController:
    def __init__(self):
        self.__game_view = GameView()
        self.__tree_controller = TreeController(self)

    
    