from typing import Union

from vbml import Pattern
from vkbottle.dispatch.rules import ABCRule
from vkbottle.user import Message

from vkreborn.vbml import patcher


class AliasRule(ABCRule[Message]):
    def __init__(
        self,
        aliases: Union[list[str], str],
        args: Union[list[str], str, None] = None,
        prefix: str = "<_:prefix>",
    ):
        if type(aliases) is str:
            aliases = [aliases]
        if type(args) is str:
            args = [args]
        self.aliases = aliases
        self.args = " ".join(args) if args else None
        self.prefix = prefix

    async def check(self, event: Message) -> bool:
        for alias in self.aliases:
            pattern_line = f"{self.prefix}{alias}"

            if self.args is not None:
                pattern_line = f"{pattern_line} {self.args}"

            pattern = Pattern(pattern_line)

            result = patcher.check(pattern, event.text)

            if result not in (False, None):
                return result

        return False
