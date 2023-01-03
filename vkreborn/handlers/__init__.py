from vkreborn.handlers import fixlayout, whoami

labelers = {
    fixlayout.labeler,
    whoami.labeler,
}

__all__ = ["labelers"]
