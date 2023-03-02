from vkreborn.handlers.general.dupe import dupecheck, dupecountall, dupecounthere

dupe_labelers = {dupecheck.labeler, dupecountall.labeler, dupecounthere.labeler}

__all__ = ["dupe_labelers"]
