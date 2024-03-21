from command_interface import Command

class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device
    
    def execute(self):
        self.device.turn_on()

class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device
    
    def execute(self):
        self.device.turn_off()

class AdjustVolumeCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.adjust_volume()

class ChangeChannelCommand(Command):
    def __init__(self, tv):
        self.tv = tv
    
    def execute(self):
        self.tv.change_channel()