import PySimpleGUI as sg

class TreeView:
    def __init__(self, tree_controller):
        self.__tree_controller = tree_controller
        self.__window = None

    def get_theme(self, themes):
        layout = [
            [sg.Text("Inclusão de tema", font=("Helvica", 25))],
            [sg.Text("Temas já existentes: " + ", ".join(themes), size = (40, 1))],
            [sg.Text("Digite o novo tema: ", size = (40,1)),
             sg.InputText("", key="theme")],
            [sg.Text("Digite um exemplo desse tema: ", size = (40,1)),
             sg.InputText("", key="example")],
            [sg.Button("Confirmar")]
        ]
        self.__window = sg.Window("Jogo - Inclusão de tema").Layout(layout)
        while True:
            button, values = self.open()
            try:
                if values["theme"] in themes:
                    raise ValueError
            except ValueError:
                sg.popup("Tema ja incluso!")
                continue
            else:
                return {"theme": values["theme"].lower(), "example": values["example"]}


    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()