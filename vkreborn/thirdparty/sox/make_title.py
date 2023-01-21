from vkreborn.thirdparty.sox.effects import BaseEffect


async def make_title(title: str, *effects: list[BaseEffect]):
    effect_names = [effect.fx_name for effect in effects if effect.fx_name]
    return f"{title} +| {', '.join(effect_names)}"
