import PySimpleGUI as sg

class TreeView:
    def __init__(self, tree_controller):
        self.__tree_controller = tree_controller
        self.__window = None

    def get_theme(self, themes):
        layout = [
            [sg.Text("Inclusão de tema", font=("Helvica", 25))],
            [sg.Text("Temas já existentes: " + ", ".join(themes), font=("Helvica", 20), size = (40, 1)), ],
            [sg.Text("Digite o novo tema: ", font=("Helvica", 15), size = (40,1)),
             sg.InputText("", key="theme")],
            [sg.Text("Digite um exemplo desse tema: ", font=("Helvica", 15), size = (40,1)),
             sg.InputText("", key="example")],
            [sg.Button("Confirmar")]
        ]
        self.__window = sg.Window("Jogo - Inclusão de tema").Layout(layout)
        while True:
            button, values = self.open()
            try:
                if not values["theme"]:
                    raise ValueError("Por favor, digite o tema!")
                if not values["example"]:
                    raise ValueError("Por favor, digite um exemplo!")
                if values["theme"] in themes:
                    raise ValueError("Tema já incluso!")
            except ValueError as err:
                sg.popup(err)
                continue
            else:
                self.close()
                return {"theme": values["theme"].capitalize(), "example": values["example"].capitalize()}

    def get_node_info(self, node):
        layout = [
            [sg.Text("Aprendi algo novo!", font=("Helvica", 25))],
            [sg.Text("Você pensou em: ", font=("Helvica", 15)),
             sg.InputText("", key="user_answer")],
            [sg.Text(f"Eu chutei: {node.key}", font=("Helvica", 15))],
            [sg.Text("Como que se diferencia a coisa que você pensou, e a que eu chutei?", font=("Helvica", 15))],
            [sg.Text("Exemplo: Se eu chutei 'baleia' e você pensou em 'gato', escreva: 'ele mia', ou 'ele vive na terra'.", font=("Helvica", 15))],
            [sg.Text("Resposta: ", font=("Helvica", 15)),
             sg.InputText("", key="user_question")],
            [sg.Button("Confirmar")]
        ]
        self.__window = sg.Window("Jogo - Inclusão de novo objeto!").Layout(layout)
        while True:
            button, values = self.open()
            try:
                if not values["user_answer"]:
                    raise ValueError("Por favor, digite o que você pensou!")
                if not values["user_question"]:
                    raise ValueError("Por favor, digite uma diferença entre os dois!")
            except ValueError as err:
                sg.popup(err)
                continue
            else:
                self.close()
                return {"user_answer": values["user_answer"].capitalize(), "user_question": values["user_question"].capitalize()}

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()