class BaseEffect:
    def filter(self) -> str:
        return ""

    def fx_name(self) -> str:
        return ""

    @staticmethod
    def _get_gain_string(gain: str) -> str:
        return gain if gain.lower().endswith("db") else f"{gain}db"
