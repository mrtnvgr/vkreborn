from vkbottle.user import UserLabeler
from vkreborn.rules import AdminRule, NewUserRule, MutedRule, ReplyMessageRule
from vkreborn.vbml import patcher

labeler = UserLabeler()
labeler.vbml_patcher = patcher
labeler.custom_rules["admin"] = AdminRule
labeler.custom_rules["new_user"] = NewUserRule
labeler.custom_rules["muted"] = MutedRule
labeler.custom_rules["reply"] = ReplyMessageRule
