from typing import Any
from orm import *
import inspect


class BaseEntity:
    pass

class Attribute:
    _type: type
    _value: object
    _nullable: bool
    _pk: bool
    _name: str

    def __init__(self, type: type, nullable: bool = True, pk: bool = False) -> None:
        self._type = type
        self._nullable = nullable
        self._pk = pk
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self._name)

    def __set__(self, instance, value):
        if value is None and not self._nullable:
            raise ValueError(f"{self._name} cannot be None")
        if value is not None and not isinstance(value, self._type):
            raise TypeError(f"{self._name} must be of type {self._type.__name__}")
        print(f"Setting {self._name} to {value}")
        instance.__dict__[self._name] = value


class Int(Attribute):
    def __init__(self, nullable: bool = True, pk: bool = False) -> None:
        super().__init__(int, nullable, pk)


class String(Attribute):
    def __init__(self, nullable: bool = True, pk: bool = False) -> None:
        super().__init__(str, nullable, pk)

class ManyToMany(Attribute):
    _entity: BaseEntity
    def __init__(self, entity: BaseEntity, nullable: bool = True, pk: bool = False) -> None:
        self._entity = entity
        super().__init__(type, nullable, pk)



class User(BaseEntity):
    id: Int = Int(nullable=False, pk=True)
    name: String = String(nullable=False)
    password: String = String(nullable=False)
    friends: 'ManyToMany' = ManyToMany(entity='User', nullable=True, pk=False)

def get_descriptors(cls):
    return {
        name: attr
        for name, attr in cls.__dict__.items()
        if isinstance(attr, Attribute)
    }

# Usage
descriptors = get_descriptors(User)

for name, descriptor in descriptors.items():
    print(f"{name}: type={descriptor._type.__name__}, nullable={descriptor._nullable}, pk={descriptor._pk}")
