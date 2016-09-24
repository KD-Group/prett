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
        self.parent = parent
        if parent is not None:
            self.parent.children.append(self)
            self.parent.changed.connect(self.check_change)

    def get_value(self):
        if self.parent is not None:
            return self.parent.get_property(self.name)
        else:
            return self.self_storage

    def set_value(self, value):
        if self.parent is not None:
            self.parent.set_property(self.name, value)
        else:
            self.self_storage = value

    @property
    def name(self) -> str:
        return self.create(str)

    @name.setter
    def name(self, value):
        self.assign(value)

    @property
    def self_storage(self):
        return self.create(object)

    @self_storage.setter
    def self_storage(self, value):
        self.assign(value)


class StringProjectItem(AbstractProjectItem, StringItemInterface):
    pass


class IntProjectItem(AbstractProjectItem, StringIntItemInterface):
    pass


class FloatProjectItem(AbstractProjectItem, StringFloatItemInterface):
    pass
