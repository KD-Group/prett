from . import AttachAbility

from . import StringItem
from . import StringIntItemInterface
from . import StringFloatItemInterface

from . import StringProperty
from . import StringIntProperty
from . import StringFloatProperty

from . import IntItem
from . import IntProperty

from . import StringListItem
from . import StringListProperty

from . import DictItem
from . import DictProperty
from . import DictListItem
from . import DictListProperty


class WidgetStringItem(StringItem, StringIntItemInterface, StringFloatItemInterface):
    pass


class WidgetStringInterface(AttachAbility):
    class StringItem(WidgetStringItem):
        pass

    @property
    def string_item(self) -> StringItem:
        return self.create(type(self).StringItem, args=(self, ))

    @property
    def string(self) -> StringProperty:
        return self.string_item.string

    @property
    def int(self) -> StringIntProperty:
        return self.string_item.int

    @property
    def float(self) -> StringFloatProperty:
        return self.string_item.float


class IndexItem(IntItem):
    pass


class WidgetIndexInterface(AttachAbility):
    class IndexItem(IndexItem):
        pass

    @property
    def index_item(self) -> IndexItem:
        return self.create(type(self).IndexItem, args=(self, ))

    @property
    def index(self) -> IntProperty:
        return self.index_item.int


class StringsItem(StringListItem):
    pass


class WidgetStringListInterface(AttachAbility):
    class StringsItem(StringsItem):
        pass

    @property
    def strings_item(self) -> StringsItem:
        return self.create(type(self).StringsItem, args=(self, ))

    @property
    def string_list(self) -> StringListProperty:
        return self.strings_item.string_list


class WidgetDictListInterface(AttachAbility):
    class DictListItem(DictListItem):
        pass

    @property
    def dict_list_item(self) -> DictListItem:
        return self.create(type(self).DictListItem, args=(self, ))

    @property
    def dict_list(self) -> DictListProperty:
        return self.dict_list_item.dict_list


class WidgetDictItem(DictItem):
    pass


class WidgetDictInterface(AttachAbility):
    class DictItem(DictItem):
        pass

    @property
    def dict_item(self) -> DictItem:
        return self.create(type(self).DictItem, args=(self, ))

    @property
    def dict(self) -> DictProperty:
        return self.dict_item.dict
