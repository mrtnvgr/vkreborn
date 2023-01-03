from vkreborn.handlers import fixlayout, new_user, whoami

labelers = {
    fixlayout.labeler,
    new_user.labeler,
    whoami.labeler,
}

__all__ = ["labelers"]
