from calc_units import bar_to_pascal, pascal_to_bar
import tkinter


class IdealesGasgesetz:
    @staticmethod
    def calc_volume(masse, spez_gaskonstante, temperatur, druck):
        volumen = (masse * spez_gaskonstante * temperatur) / druck
        return volumen

    @staticmethod
    def ask_for_variables():
        masse = float(input("Bitte Masse angeben: "))
        spez_gaskonstante = float(input("Bitte spez. Gaskonstante angeben: "))
        temperatur = float(input("Bitte Temperatur angeben: "))
        druck = float(input("Bitte Druck Bar angeben: "))
        return masse, spez_gaskonstante, temperatur, druck


def quit():
    exit(0)


Commands = {
    "quit": quit
}

if __name__ == '__main__':
    while True:
        command = input(">").lower().split(" ")
        if command[0] in Commands:
            Commands[command[0]]()
        else:
            print("Was möchtest du berechnen lassen?: ")
