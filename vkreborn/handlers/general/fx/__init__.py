from vkreborn.handlers.general.fx import bass, fx, reverb, reverse, tempo
from vkreborn.handlers.general.fx.core import core_labelers

fx_labelers = {
    fx.labeler,
    *core_labelers,
    tempo.labeler,
    bass.labeler,
    reverse.labeler,
    reverb.labeler,
}

__all__ = ["fx_labelers"]
