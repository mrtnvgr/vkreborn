from vkreborn.config import FX_BASS_GAIN
from vkreborn.thirdparty.sox.effects import BaseEffect


class BassEffect(BaseEffect):
    def __init__(self, gain: float = FX_BASS_GAIN):
        self.gain = gain

    @property
    def filter(self) -> str:
        return f"bass {self.gain}"

    @property
    def fx_name(self) -> str:
        if self.gain > 1:
            return "bassboost"
        elif self.gain < 1:
            return "basscut"
        else:
            return ""
