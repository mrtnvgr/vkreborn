from vkreborn.handlers import fixlayout, whoami, admins, roll

labelers = {
    fixlayout.labeler,
    whoami.labeler,
    admins.labeler,
    roll.labeler,
}

__all__ = ["labelers"]
