from vkreborn.handlers import (
    new_user,
    muted,
    fixlayout,
    whoami,
    moders,
    roll,
    trans,
    shazam,
    wallhaven,
    helphandler,
)

from vkreborn.handlers.for_moders import moder_labelers
from vkreborn.handlers.for_owner import owner_labelers

labelers = {
    *owner_labelers,
    *moder_labelers,
    new_user.labeler,
    muted.labeler,
    fixlayout.labeler,
    whoami.labeler,
    moders.labeler,
    roll.labeler,
    trans.labeler,
    shazam.labeler,
    wallhaven.labeler,
    helphandler.labeler,
}

__all__ = ["labelers"]
