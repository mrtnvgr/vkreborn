from vkreborn.handlers.general.fx import bass, core, fx, reverse

fx_labelers = {
    fx.labeler,
    core.labeler,
    bass.labeler,
    reverse.labeler,
}

__all__ = ["fx_labelers"]
