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

    def show_tutorial(self):
        sg.popup(("Para jogar: Pense em algo baseado no tema escolhido, e eu tentarei advinhar o que fo pensado. Se eu acertar, você pensa em outra coisa, se eu errar, você me diz o que pensou e o que difere isso do meu chute!"))

    def reset_warning(self):
        layout = [
            [sg.Text("ATENÇÃO! Você está prestes a apagar todas os temas!")],
            [sg.Text("Será necessário inserir cada tema e dado manualmente novamente!")],
            [sg.Button("Confirmar"), sg.Cancel("Cancelar")]
        ]
        self.__window = sg.Window("Resetar").Layout(layout)
        button, values = self.open()
        if button in (None, "Confirmar"):
            self.close()
            return 1
        self.close()
        return 0

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()