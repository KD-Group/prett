import typing

from . import AbstractItem
from . import AbstractProperty
from . import ValueModel


class StringValueModel(ValueModel):
    @property
    def value(self) -> str:
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(value)


class StringProperty(AbstractProperty, StringValueModel):
    pass


class StringItemInterface(AbstractItem):
    @property
    def string(self) -> StringProperty:
        return self.create(StringProperty, args=(self,))


class StringItem(StringItemInterface):
    pass


class IntValueModel(ValueModel):
    @property
    def value(self) -> int:
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(int(value))


class IntProperty(AbstractProperty, IntValueModel):
    pass


class IntItemInterface(AbstractItem):
    @property
    def int(self) -> IntProperty:
        return self.create(IntProperty, args=(self,))


class IntItem(IntItemInterface):
    pass


class FloatValueModel(ValueModel):
    @property
    def value(self) -> float:
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(float(value))


class FloatProperty(AbstractProperty, FloatValueModel):
    pass


class FloatItemInterface(AbstractItem):
    @property
    def float(self) -> FloatProperty:
        return self.create(FloatProperty, args=(self,))


class FloatItem(FloatItemInterface):
    pass


class DictValueModel(ValueModel):
    @property
    def value(self) -> dict:
        if self.get_value() is None:
            return {}
        if isinstance(self.get_value(), dict):
            return self.get_value()
        else:
            return eval(self.get_value())

    @value.setter
    def value(self, value):
        self.set_value(value)


class DictProperty(AbstractProperty, DictValueModel):

    def __setitem__(self, key, value):
        self.value.__setitem__(key, value)
        self.parent.emit_changed()
        self.emit_changed()

    def __getitem__(self, item):
        return self.value.__getitem__(item)

    def __getattr__(self, attr_name):
        if not self.__dict__.__contains__(attr_name) and attr_name in dir(self.value):
            def wrapper(*args, **kwargs):
                previous_value = self.value.copy()
                return_value = getattr(self.value, attr_name)(*args, **kwargs)
                if previous_value != self.value:
                    # print(self)
                    self.parent.emit_changed()
                    self.emit_changed()
                return return_value

            return wrapper
        return self.__getattribute__(attr_name)


class DictItemInterface(AbstractItem):

    @property
    def dict(self) -> DictProperty:
        return self.create(DictProperty, args=(self,))


class DictItem(DictItemInterface):
    pass


class DictListValueModel(ValueModel):
    @property
    def value(self) -> typing.List[dict]:
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(value)

    @property
    def count(self):
        return len(self.value)


class DictListProperty(AbstractProperty, DictListValueModel):
    pass


class DictListItemInterface(AbstractItem):
    @property
    def dict_list(self) -> DictListProperty:
        return self.create(DictListProperty, args=(self,))


class DictListItem(DictListItemInterface):
    pass


class ListValueModel(ValueModel):
    @property
    def value(self) -> list:
        if self.get_value() == '' or self.get_value() is None:
            return []
        if isinstance(self.get_value(), str):
            return eval(self.get_value())
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(value)


class ListProperty(AbstractProperty, ListValueModel):
    def __setitem__(self, key, value):
        self.value.__setitem__(key, value)
        self.parent.emit_changed()
        self.emit_changed()

    def __getitem__(self, item):
        return self.value.__getitem__(item)

    def __getattr__(self, attr_name):
        if not self.__dict__.__contains__(attr_name) and attr_name in dir(self.value):
            def wrapper(*args, **kwargs):
                previous_value = self.value.copy()
                return_value = getattr(self.value, attr_name)(*args, **kwargs)
                if previous_value != self.value:
                    self.parent.emit_changed()
                    self.emit_changed()
                return return_value

            return wrapper
        return self.__getattribute__(attr_name)

    pass


class ListItemInterface(AbstractItem):

    @property
    def list(self) -> ListProperty:
        return self.create(ListProperty, args=(self,))


class ListItem(ListItemInterface):
    pass


class StringListValueModel(ValueModel):
    @property
    def value(self) -> typing.List[str]:
        return self.get_value()

    @value.setter
    def value(self, value):
        self.set_value(value)

    @property
    def count(self):
        return len(self.value)


class StringListProperty(AbstractProperty, StringListValueModel):
    pass


class StringListItemInterface(AbstractItem):
    @property
    def string_list(self) -> StringListProperty:
        return self.create(StringListProperty, args=(self,))


class StringListItem(StringListItemInterface):
    pass


class StringIntProperty(IntProperty):
    def get_value(self):
        return int(self.parent.get_value())

    def set_value(self, value):
        self.parent.set_value(str(value))


class StringIntItemInterface(StringItemInterface):
    @property
    def int(self) -> StringIntProperty:
        return self.create(StringIntProperty, args=(self,))


class StringFloatProperty(FloatProperty):
    def get_value(self):
        if self.parent.get_value() == '':
            return None
        return float(self.parent.get_value())

    def set_value(self, value):
        self.parent.set_value(str(value))


class StringFloatItemInterface(StringItemInterface):
    @property
    def float(self) -> StringFloatProperty:
        return self.create(StringFloatProperty, args=(self,))
