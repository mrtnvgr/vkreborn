from vkreborn.handlers.general import (
    demotivator,
    fixlayout,
    helphandler,
    mix,
    moders,
    muted,
    mutedby,
    qrcreate,
    qrread,
    roll,
    shazam,
    tiktok,
    tinyurl,
    trans,
    wallhaven,
    whoami,
    whois,
    whomuted,
)
from vkreborn.handlers.general.dupe import dupe_labelers
from vkreborn.handlers.general.fx import fx_labelers

general_labelers = {
    muted.labeler,
    mutedby.labeler,
    mix.labeler,
    whomuted.labeler,
    demotivator.labeler,
    *dupe_labelers,
    *fx_labelers,
    fixlayout.labeler,
    whoami.labeler,
    whois.labeler,
    moders.labeler,
    roll.labeler,
    trans.labeler,
    shazam.labeler,
    tiktok.labeler,
    wallhaven.labeler,
    qrcreate.labeler,
    qrread.labeler,
    tinyurl.labeler,
    helphandler.labeler,
}

__all__ = ["general_labelers"]
