from vkreborn.handlers import (
    new_user,
    fixlayout,
    whoami,
    admins,
    roll,
    trans,
)

from vkreborn.handlers.for_admins import admin_labelers
from vkreborn.handlers.for_owner import owner_labelers

labelers = {
    *owner_labelers,
    *admin_labelers,
    new_user.labeler,
    fixlayout.labeler,
    whoami.labeler,
    admins.labeler,
    roll.labeler,
    trans.labeler,
}

__all__ = ["labelers"]
