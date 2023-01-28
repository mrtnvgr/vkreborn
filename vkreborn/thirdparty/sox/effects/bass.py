from typing import Optional

from vkreborn.config import FX_BASS_GAIN
from vkreborn.thirdparty.sox.effects import BaseEffect


class BassEffect(BaseEffect):
    def __init__(self, gain: Optional[float]):
        if gain is None:
            self.gain = FX_BASS_GAIN
            self.default = True
        else:
            self.gain = gain
            self.default = False

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
