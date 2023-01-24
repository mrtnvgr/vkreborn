from vkreborn.thirdparty.sox.effects import BaseEffect


class ReverseEffect(BaseEffect):
    @property
    def filter(self) -> str:
        return "reverse"

    @property
    def fx_name(self) -> str:
        return "reverse"
