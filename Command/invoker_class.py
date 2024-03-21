from command_interface import Command

class RemoteControl:
    def __init__(self):
        self.command = None

    def execute_command(self, command: Command):
        self.command = command
        if self.command:
            self.command.execute()
        else:
            print("Não há comandos.")