from node import Node

class DecisionTree:
    def __init__(self):
        self.__root = None

    def start_game(self):
        print("TUTORIAL: O jogo funciona da seguinte maneira: Você pensa em algo, e eu tento adivinhar.")
        print("Primeiramente será escolhido um tema.")
        print("Depois, você dará um exemplo desse tema, para começar o jogo.")
        print("E então, eu tentarei adivinhar o que você está pensando sobre esse tema.")
        print("Caso eu erre, você me dirá o que pensou, e qual a diferença entre ele e o que eu chutei.")

        tema = input("Qual o tema do jogo? (Escreva no singular. Ex: Animal, Jogador de Futebol, Jogo Eletronico): ")
        print(tema)


class Main():

    tree = DecisionTree()
    tree.start_game()