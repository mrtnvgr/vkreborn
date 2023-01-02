from vkreborn.handlers import fixlayout, new_user

labelers = {
    fixlayout.labeler,
    new_user.labeler,
}

__all__ = ["labelers"]
