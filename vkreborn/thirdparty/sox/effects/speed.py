from typing import Optional

from vkreborn.config import FX_DAYCORE_SPEED, FX_NIGHTCORE_SPEED
from vkreborn.thirdparty.sox.effects import BaseEffect


class SpeedEffect(BaseEffect):
    def __init__(self, speed: Optional[float | str]):
        super().__init__()
        self.default = True if type(speed) is str else False

        default_speeds = {
            "nightcore": FX_NIGHTCORE_SPEED,
            "daycore": FX_DAYCORE_SPEED,
        }
        self.speed = default_speeds.get(speed, speed)

    @property
    def filter(self) -> str:
        return f"speed {self.speed}"

    @property
    def fx_name(self) -> str:
        if self.speed == 1:
            speed = ""
        elif self.speed > FX_DAYCORE_SPEED:
            speed = "nightcore"
        else:
            speed = "daycore"

        if speed and not self.default:
            speed += f" x{self.speed}"

        return speed
