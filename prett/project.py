import os
import time
import json
import codecs
from . import *
import typing


class SaveInterface(ValueModel):
    def load(self, check_key: str, check_value: str):
        if not os.path.exists(self.filename):
            raise FileNotFoundError('Setting File [{}] Not Found'.format(self.filename))

        try:
            with codecs.open(self.filename, 'r', encoding='utf-8') as f:
                obj = json.load(f)
                assert isinstance(obj, dict)
                assert obj.get(check_key, None) == check_value
                self.value = obj
        except AssertionError as e:
            raise e
        except ValueError as e:
            raise e

    def save(self):
        with codecs.open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.value, f, indent=2, ensure_ascii=False)

    @property
    def path(self) -> typing.Optional[str]:
        return None

    @property
    def name(self) -> typing.Optional[str]:
        return None

    @property
    def filename(self):
        return os.path.join(self.path, self.name)

    @property
    def is_existing(self):
        return os.path.exists(self.filename)


class AbstractProject(DictValueModel, SaveInterface, ChangedInterface):
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


class AbstractProjectItem(StringItemInterface):
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
            self.check_change()

    @property
    def name(self) -> str:
        return self.create(str)

    @name.setter
    def name(self, value):
        self.assign(value)

    @property
    def self_storage(self):
        return self.create(lambda: None)

    @self_storage.setter
    def self_storage(self, value):
        self.assign(value)


class StringProjectItem(AbstractProjectItem):
    pass


class IntProjectItem(AbstractProjectItem, StringIntItemInterface):
    pass


class FloatProjectItem(AbstractProjectItem, StringFloatItemInterface):
    pass


class TimePointItem(StringProjectItem):
    class TimePointProperty(StringProperty):
        def update(self):
            self.value = time.strftime("%y-%m-%d %H:%M:%S")

    @property
    def time(self) -> TimePointProperty:
        return self.create(TimePointItem.TimePointProperty, args=(self, ))
