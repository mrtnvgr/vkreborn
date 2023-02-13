from vkreborn.handlers.general.fx import fx, reverb, reverse, tempo, volume
from vkreborn.handlers.general.fx.bass import bass_labelers
from vkreborn.handlers.general.fx.core import core_labelers

fx_labelers = {
    fx.labeler,
    *core_labelers,
    tempo.labeler,
    *bass_labelers,
    reverse.labeler,
    reverb.labeler,
    volume.labeler,
}

__all__ = ["fx_labelers"]
