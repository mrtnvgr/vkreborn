from vkreborn.handlers import new_user, fixlayout, whoami, admins, roll, mute

labelers = {
    new_user.labeler,
    fixlayout.labeler,
    whoami.labeler,
    admins.labeler,
    roll.labeler,
    mute.labeler,
}

__all__ = ["labelers"]
