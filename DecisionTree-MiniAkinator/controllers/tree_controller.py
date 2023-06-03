from models.decision_tree import DecisionTree
from models.node import Node
from data_access_objects.tree_dao import TreeDAO
from views.tree_view import TreeView

class TreeController():
    def __init__(self, game_controller):
        self.__game_controller = game_controller
        self.__tree_view = TreeView(self)
        self.__tree_dao = TreeDAO("tree.pkl")

    def include_theme(self):
        theme_data = self.__tree_view.get_theme(self.get_themes())
        tree = DecisionTree(Node(theme_data["example"], True), theme_data["theme"])
        self.__tree_dao.add(tree)

    def get_themes(self):
        themes = []
        for tree in self.__tree_dao.get_all():
            themes.append(tree.theme)
        return themes
    
    def search_tree_by_theme(self, chosen_theme):
        for tree in self.__tree_dao.get_all():
            if tree.theme == chosen_theme:
                return tree

    def add_new_node(self, node):
        node_data = self.__tree_view.get_node_info(node)
        temp = node.key
        node.key = f'{node_data["user_question"]}?'
        node.left = Node(temp, True)
        node.right = Node(node_data["user_answer"], True)
        node.isleaf = False

    def reset_themes(self):
        self.__tree_dao.reset()

    def update(self, tree):
        self.__tree_dao.update(tree)
