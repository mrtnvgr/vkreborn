from vkreborn.thirdparty.sox.effects import BaseEffect


class RawEffect(BaseEffect):
    def __init__(self, effects: str):
        self.effects = effects

    @property
    def filter(self) -> str:
        return self.effects

    @property
    def fx_name(self) -> str:
        return f'raw "{self.effects}"'
