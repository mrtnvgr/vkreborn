from vkreborn.handlers import new_user, fixlayout, whoami, admins, roll

labelers = {
    new_user.labeler,
    fixlayout.labeler,
    whoami.labeler,
    admins.labeler,
    roll.labeler,
}

__all__ = ["labelers"]
