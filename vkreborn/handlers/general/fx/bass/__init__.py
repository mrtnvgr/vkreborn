from vkreborn.handlers.general.fx.bass import bass, bassboost, basscut

bass_labelers = {
    bass.labeler,
    bassboost.labeler,
    basscut.labeler,
}

__all__ = ["bass_labelers"]
