from vkreborn.handlers.for_owner.dupe import (
    dupeclear,
    dupeclearall,
    dupeclearold,
    dupegroups,
    dupeoff,
    dupeon,
)

dupe_labelers = {
    dupeon.labeler,
    dupeoff.labeler,
    dupegroups.labeler,
    dupeclearall.labeler,
    dupeclearold.labeler,
    dupeclear.labeler,
}

__all__ = ["dupe_labelers"]
