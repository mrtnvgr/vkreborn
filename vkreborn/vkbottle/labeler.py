from vkbottle.user import UserLabeler
from vkreborn.rules import AdminRule
from vkreborn.vbml import patcher

labeler = UserLabeler()
labeler.vbml_patcher = patcher
labeler.custom_rules["admin"] = AdminRule()
