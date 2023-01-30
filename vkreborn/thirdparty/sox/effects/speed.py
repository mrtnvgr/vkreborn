from typing import Optional

from vkreborn.config import (
    FX_DAYCORE_SPEED,
    FX_NIGHTCORE_SPEED,
    FX_SOFTDAYCORE_SPEED,
    FX_SOFTNIGHTCORE_SPEED,
)
from vkreborn.thirdparty.sox.effects import BaseEffect


class SpeedEffect(BaseEffect):
    def __init__(self, speed: Optional[float | str]):
        self.default = True if type(speed) is str else False

        self.default_speeds = {
            "daycore": FX_DAYCORE_SPEED,
            "softdaycore": FX_SOFTDAYCORE_SPEED,
            "softnightcore": FX_SOFTNIGHTCORE_SPEED,
            "nightcore": FX_NIGHTCORE_SPEED,
        }
        self.speed = self.default_speeds.get(speed, speed)

    @property
    def filter(self) -> str:
        return f"speed {self.speed}"

    @property
    def fx_name(self) -> str:
        if self.speed == 1:
            return ""
        elif self.speed <= FX_DAYCORE_SPEED:
            speed = "daycore"
        elif self.speed <= FX_SOFTDAYCORE_SPEED:
            speed = "soft daycore"
        elif self.speed <= FX_SOFTNIGHTCORE_SPEED:
            speed = "soft nightcore"
        else:
            speed = "nightcore"

        if speed and not self.default:
            speed += f" x{self.speed}"

        return speed
