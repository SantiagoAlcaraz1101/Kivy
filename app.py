from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class TrikiApp( App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.turno: bool = False
        self.tablero: dict = {}
    
    def build(self):
        tablero = BoxLayout()
        

        for i in range(3):
            columna = BoxLayout(orientation = "vertical")
            tablero.add_widget(columna)

            for j in range(3):
                casilla = Button(font_size = "50")
                casilla.posicion = (i,j)
                self.tablero[casilla.posicion] = None
                columna.add_widget(casilla)
                casilla.bind(on_press = self.seleccionar_casilla)
        return tablero
    
    def seleccionar_casilla(self, sender):
        if self.turno:
            sender.text = "O"
            self.tablero[sender.posicion] = sender.text
        else:
            sender.text = "X"
            self.tablero[sender.posicion] = sender.text

        self.turno = not self.turno

if __name__ == "__main__":
    TrikiApp().run()