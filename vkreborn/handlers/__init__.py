from vkreborn.handlers.general import general_labelers
from vkreborn.handlers.for_moders import moder_labelers
from vkreborn.handlers.for_owner import owner_labelers

labelers = {
    *owner_labelers,
    *moder_labelers,
    *general_labelers,
}

__all__ = ["labelers"]
