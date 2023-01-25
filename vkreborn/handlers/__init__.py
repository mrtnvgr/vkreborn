from vkreborn.handlers import (
    fixlayout,
    helphandler,
    moders,
    muted,
    new_user,
    roll,
    shazam,
    trans,
    wallhaven,
    whoami,
)
from vkreborn.handlers.for_moders import moder_labelers
from vkreborn.handlers.for_owner import owner_labelers
from vkreborn.handlers.fx import fx_labelers

labelers = {
    *owner_labelers,
    *moder_labelers,
    new_user.labeler,
    muted.labeler,
    *fx_labelers,
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
