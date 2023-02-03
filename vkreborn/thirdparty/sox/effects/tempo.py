from vkreborn.thirdparty.sox.effects import BaseEffect


class TempoEffect(BaseEffect):
    def __init__(self, tempo: float):
        self.tempo = tempo

    @property
    def filter(self) -> str:
        return f"tempo {self.tempo}"

    @property
    def fx_name(self) -> str:
        return f"tempo x{self.tempo}"
