from . import AbstractProject
from . import AbstractProjectItem
from . import DictItemInterface
from . import StringFloatItemInterface
from . import StringIntItemInterface
from . import StringItemInterface
from . import StringListItemInterface


class AbstractSetting(AbstractProject):
    pass


class AbstractSettingItem(AbstractProjectItem):
    def __init__(self, parent: AbstractSetting, default_value=None):
        super().__init__(parent)

        if default_value is not None:
            if isinstance(default_value, list):
                self.self_storage = default_value
            else:
                self.self_storage = str(default_value)

    def get_value(self):
        if self.parent is not None:
            ret = self.parent.get_property(self.name)
            if ret is not None:
                return ret
        return self.self_storage


class StringSettingItem(AbstractSettingItem, StringItemInterface):
    pass


class StringListSettingItem(AbstractSettingItem, StringListItemInterface):
    pass


class IntSettingItem(AbstractSettingItem, StringIntItemInterface):
    pass


class FloatSettingItem(AbstractSettingItem, StringFloatItemInterface):
    pass


class DictSettingItem(AbstractSettingItem, DictItemInterface):
    pass
