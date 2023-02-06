from vkreborn.handlers.for_owner import whgreset
from vkreborn.handlers.for_owner.dupe import dupe_labelers

owner_labelers = {whgreset.labeler, *dupe_labelers}

__all__ = ["owner_labelers"]
