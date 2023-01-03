from vkreborn.handlers import fixlayout, whoami, admins

labelers = {
    fixlayout.labeler,
    whoami.labeler,
    admins.labeler,
}

__all__ = ["labelers"]
