from typing import Optional

from vkreborn.thirdparty.sox.effects import BaseEffect


class ReverbEffect(BaseEffect):
    def __init__(self, wet: Optional[float] = None):
        self.default = False if wet else True
        self.wet = wet if wet else 80

    @property
    def filter(self) -> str:
        return f"reverb {self.wet}"

    @property
    def fx_name(self) -> str:
        return f"reverb {self.wet:g}%" if not self.default else "reverb"
