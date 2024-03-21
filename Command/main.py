from concrete_command_classes import TurnOnCommand, TurnOffCommand, AdjustVolumeCommand, ChangeChannelCommand
from receiver_classes import TV, Stereo, Lamp
from invoker_class import RemoteControl

if __name__ == "__main__":

    tv = TV()
    stereo = Stereo()
    lamp = Lamp()


    turn_on_tv_command = TurnOnCommand(tv)
    turn_off_tv_command = TurnOffCommand(tv)
    change_channel_tv_command = ChangeChannelCommand(tv)
    turn_on_stereo_command = TurnOnCommand(stereo)
    turn_off_stereo_command = TurnOffCommand(stereo)
    adjust_volume_stereo_command = AdjustVolumeCommand(stereo)
    turn_on_lamp_command = TurnOnCommand(lamp)
    turn_off_lamp_command = TurnOffCommand(lamp)


    remote = RemoteControl()


    remote.execute_command(TurnOnCommand(tv))
    remote.execute_command(ChangeChannelCommand(tv))
    remote.execute_command(TurnOffCommand(tv))
    remote.execute_command(AdjustVolumeCommand(stereo))
    remote.execute_command(TurnOnCommand(stereo))
    remote.execute_command(AdjustVolumeCommand(stereo))
    remote.execute_command(TurnOffCommand(stereo))
    remote.execute_command(TurnOnCommand(lamp))
    remote.execute_command(TurnOffCommand(lamp))