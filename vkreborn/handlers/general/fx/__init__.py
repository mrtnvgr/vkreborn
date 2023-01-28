from vkreborn.handlers.general.fx import bass, core, fx, reverb, reverse

fx_labelers = {
    fx.labeler,
    core.labeler,
    bass.labeler,
    reverse.labeler,
    reverb.labeler,
}

__all__ = ["fx_labelers"]
