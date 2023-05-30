import PySimpleGUI as sg

class GameView:
    def __init__(self, game_controller):
        self.__game_controller = game_controller
        self.__window = None

    def show_options(self):
        sg.theme("DarkBlue2")
        layout = [
            [sg.Text("Jogo de advinhação", font=("Helvica", 25))],
            [sg.Text("O que gostaria de fazer?", font=("Helvica", 15))],
            [sg.Radio("Jogar", "RD1", key="1")],
            [sg.Radio("Incluir novo tema", "RD1", key="2")],
            [sg.Radio("Mostrar o tutorial", "RD1", key="3")],
            [sg.Radio("Resetar os temas", "RD1", key="4")],
            [sg.OK("Confirmar"), sg.Cancel("Desligar")]
        ]
        self.__window = sg.Window("Jogo - Árvore de Decisão").Layout(layout)
        button, values = self.open()
        if button in (None, "Desligar"):
            self.close()
            return 0
        for key in values:
            if values[key]:
                self.close()
                return int(key)


    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()