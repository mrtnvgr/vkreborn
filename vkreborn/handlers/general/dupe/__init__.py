from vkreborn.handlers.general.dupe import dupecheck, dupecountall

dupe_labelers = {dupecheck.labeler, dupecountall.labeler}

__all__ = ["dupe_labelers"]
