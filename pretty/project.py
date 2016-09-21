from . import *
import typing


class AbstractProject(ValueInterface, DictValueModel, ChangedInterface):
    def get_value(self) -> dict:
        return self.create(dict)

    def set_value(self, value):
        self.value.clear()
        self.value.update(value)
        self.changed.emit(self.value)

    def get_property(self, name) -> object:
        return self.value.get(name)

    def set_property(self, name, value):
        self.value.update({name: value})
        self.changed.emit(self.value)

    # children property
    @property
    def children(self) -> typing.List['AbstractProjectItem']:
        return self.create(list)

    # name property
    def __setattr__(self, key: str, value):
        if isinstance(value, AbstractProjectItem):
            value.name = key
        super().__setattr__(key, value)


class AbstractProjectItem(AbstractItem):
    def __init__(self, parent: AbstractProject=None):
        if parent is not None:
            self.parent = parent
            self.parent.children.append(self)
            self.parent.changed.connect(self.check_change)

    def get_value(self):
        return self.parent.get_property(self.name)

    def set_value(self, value):
        self.parent.set_property(self.name, value)

    @property
    def name(self) -> str:
        return self.create(str)

    @name.setter
    def name(self, value):
        self.assign(value)


class StringProjectItem(AbstractProjectItem, StringItemInterface):
    pass


class IntProjectItem(AbstractProjectItem, StringIntItemInterface):
    pass


class FloatProjectItem(AbstractProjectItem, StringFloatItemInterface):
    pass
