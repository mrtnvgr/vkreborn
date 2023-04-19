from vkreborn.thirdparty.sox.effects import BaseEffect


class VolumeEffect(BaseEffect):
    def __init__(self, volume: float):
        self.volume = volume

    @property
    def filter(self) -> str:
        return f"vol {self.volume}"

    @property
    def fx_name(self) -> str:
        return f"volume {self._get_gain_string(self.volume)}"
