from vkbottle.user import UserLabeler

from vkreborn.rules import AttachmentRule, ModerRule, OwnerRule, ReplyMessageRule
from vkreborn.vbml import patcher

labeler = UserLabeler()
labeler.vbml_patcher = patcher
labeler.custom_rules["moder"] = ModerRule
labeler.custom_rules["attachment"] = AttachmentRule
labeler.custom_rules["owner"] = OwnerRule
labeler.custom_rules["reply"] = ReplyMessageRule
