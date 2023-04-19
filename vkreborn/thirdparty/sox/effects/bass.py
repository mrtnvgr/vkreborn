from typing import Optional

from vkreborn.config import FX_BASSBOOST_GAIN, FX_BASSCUT_GAIN
from vkreborn.thirdparty.sox.effects import BaseEffect


class BassEffect(BaseEffect):
    def __init__(self, gain: Optional[float]):
        self.default = False if type(gain) is float else True

        table = {
            "bassboost": FX_BASSBOOST_GAIN,
            "basscut": FX_BASSCUT_GAIN,
        }
        self.gain = table.get(gain, gain)

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
            name += f" {self._get_gain_string(self.gain)}"

        return name
