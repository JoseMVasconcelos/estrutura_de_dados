from models.decision_tree import DecisionTree
from models.node import Node
from data_access_objects.tree_dao import TreeDAO
from views.tree_view import TreeView

class TreeController():
    def __init__(self, game_controller):
        self.__game_controller = game_controller
        self.__tree_view = TreeView(self)
        self.__tree_dao = TreeDAO()

    def include_theme(self):
        theme_data = self.__tree_view.get_theme(self.get_themes())

        tree = DecisionTree(theme_data["theme"])
        tree.__root = Node(theme_data["example"])

        self.__tree_dao.add(tree)

    def get_themes(self):
        themes = self.__tree_dao.get_all()
        self.__tree_view.show_themes(themes)