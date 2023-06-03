import PySimpleGUI as sg

class GameView:
    def __init__(self, game_controller):
        self.__game_controller = game_controller
        self.__window = None

    def show_options(self):
        sg.theme("DarkBlue2")
        layout = [
            [sg.Text("Jogo de advinhação", font=("Helvica", 25))],
            [sg.Text("O que gostaria de fazer?", font=("Helvica", 20))],
            [sg.Radio("Jogar", "RD1", font=("Helvica", 15), key="1")],
            [sg.Radio("Incluir novo tema", "RD1", font=("Helvica", 15), key="2")],
            [sg.Radio("Mostrar o tutorial", "RD1", font=("Helvica", 15), key="3")],
            [sg.Radio("Resetar os temas", "RD1", font=("Helvica", 15), key="4")],
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
            
    def game_screen(self, node):
        layout = [
            [sg.Text("Jogo de advinhação", font=("Helvica", 25))],
            [sg.Text(node.key.capitalize(), font=("Helvica", 15))],
            [sg.Button("Sim"), sg.Button("Não")]
        ]
        self.__window = sg.Window("Jogo - Árvore de Decisão").Layout(layout)
        button, values = self.open()
        if button in (None, "Não"):
            self.close()
            return 0
        else:
            self.close()
            return 1
        
    def final_guess(self, node):
        layout = [
            [sg.Text("Jogo de advinhação", font=("Helvica", 25))],
            [sg.Text(f"Você pensou em: {node.key}?", font=("Helvica", 15))],
            [sg.Button("Sim"), sg.Button("Não")]
        ]
        self.__window = sg.Window("Jogo - Palpite final").Layout(layout)
        button, values = self.open()
        if button in (None, "Não"):
            self.close()
            return 0
        else:
            self.close()
            return 1
        
    def choose_theme(self, themes):
        layout = [
                [sg.Text("Escolha o tema", font=("Helvica", 25))],
        ]

        for theme in themes:
            layout.append(
                [sg.Radio(f"{theme.capitalize()}", "themes", font=("Helvica", 15), key = theme)]
            )
        layout.append([sg.Button("Confirmar")])

        self.__window = sg.Window("Escolha de tema").Layout(layout)
        button, values = self.open()
        for theme in values:
            if values[theme]:
                self.close()
                return theme

    def show_tutorial(self):
        sg.popup(("Para jogar: Pense em algo baseado no tema escolhido, e eu tentarei advinhar o que fo pensado. Se eu acertar, você pensa em outra coisa, se eu errar, você me diz o que pensou e o que difere isso do meu chute!"))

    def reset_warning(self):
        layout = [
            [sg.Text("ATENÇÃO! Você está prestes a apagar todas os temas!", font=("Helvica", 15))],
            [sg.Text("Será necessário inserir cada tema e dado manualmente novamente!", font=("Helvica", 15))],
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

    def show_message(self, msg):
        sg.popup(msg, font=("Helvica", 15))