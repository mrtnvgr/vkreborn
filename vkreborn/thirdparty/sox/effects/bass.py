from typing import Optional

from vkreborn.config import FX_BASS_GAIN
from vkreborn.thirdparty.sox.effects import BaseEffect


class BassEffect(BaseEffect):
    def __init__(self, gain: Optional[float]):
        self.default = False if gain else True
        self.gain = gain if gain else FX_BASS_GAIN

    @property
    def filter(self) -> str:
        return f"bass {self.gain}"

    @property
    def fx_name(self) -> str:
        if self.gain > 1:
            name = "bassboost"
        elif self.gain < 1:
            name = "basscut"
        else:
            return ""

        if not self.default:
            name += f" {self.gain}"

        return name
