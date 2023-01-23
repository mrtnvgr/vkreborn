from vkreborn.handlers.fx import fx, core, bass, reverse

fx_labelers = {
    fx.labeler,
    core.labeler,
    bass.labeler,
    reverse.labeler,
}

__all__ = ["fx_labelers"]
