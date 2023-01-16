from vkreborn.handlers import (
    new_user,
    muted,
    fixlayout,
    whoami,
    admins,
    roll,
    trans,
    shazam,
    wallhaven,
    helphandler,
)

from vkreborn.handlers.for_admins import admin_labelers
from vkreborn.handlers.for_owner import owner_labelers

labelers = {
    *owner_labelers,
    *admin_labelers,
    new_user.labeler,
    muted.labeler,
    fixlayout.labeler,
    whoami.labeler,
    admins.labeler,
    roll.labeler,
    trans.labeler,
    shazam.labeler,
    wallhaven.labeler,
    helphandler.labeler,
}

__all__ = ["labelers"]
