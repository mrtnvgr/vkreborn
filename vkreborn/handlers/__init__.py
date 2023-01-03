from vkreborn.handlers import fixlayout, new_user, whoami

labelers = {
    new_user.labeler,
    fixlayout.labeler,
    whoami.labeler,
}

__all__ = ["labelers"]
