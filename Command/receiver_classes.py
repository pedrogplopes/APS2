class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class TV(Device):
    def __init__(self):
        self.powered_on = False

    def turn_on(self):
        print("A TV foi ligada.")
        self.powered_on = True

    def turn_off(self):
        print("A TV foi desligada.")
        self.powered_on = False

    def change_channel(self):
        if self.powered_on:
            print("A TV mudou de canal.")
        else:
            print("A TV está desligada.")

class Stereo(Device):
    def __init__(self):
        self.powered_on = False

    def turn_on(self):
        print("A caixa de som foi ligada.")
        self.powered_on = True

    def turn_off(self):
        print("A caixa de som foi desligada.")
        self.powered_on = False

    def adjust_volume(self):
        if self.powered_on:
            print("O volume foi ajustado.")
        else:
            print("A caixa de som está desligada.")


class Lamp(Device):
    def turn_on(self):
        print("A lâmpada foi ligada.")

    def turn_off(self):
        print("A lâmpada foi desligada.")