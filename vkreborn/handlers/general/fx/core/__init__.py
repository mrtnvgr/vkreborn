from vkreborn.handlers.general.fx.core import (
    core,
    daycore,
    nightcore,
    softdaycore,
    softnightcore,
)

core_labelers = {
    nightcore.labeler,
    softnightcore.labeler,
    daycore.labeler,
    softdaycore.labeler,
    core.labeler,
}

__all__ = ["core_labelers"]
