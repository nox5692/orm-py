from typing import Type, Collection
from .base_orm_entity import BaseORMEntity
from .._io import ConsoleMessage


class Attribute:
    _type: type
    _value: object
    _nullable: bool
    _pk: bool
    _name: str
    _sql_type: str

    def __init__(
        self,
        type: type,
        nullable: bool = True,
        pk: bool = False,
        sql_type: str = None,
    ) -> None:
        self._type = type
        self._nullable = nullable
        self._pk = pk
        self._sql_type = sql_type
        self._name = None

    def __set_name__(
        self,
        owner,
        name,
    ):
        self._name = name

    def __get__(
        self,
        instance,
        owner,
    ):
        if instance is None:
            return self
        print(f"Getting {self._name}")
        return instance.__dict__.get(self._name)

    def __set__(
        self,
        instance,
        value,
    ):
        if value is None and not self._nullable:
            raise ValueError(
                ConsoleMessage(f"'{self._name}' is not nullable.").error()
            )
        if value is not None and not isinstance(value, self._type):
            raise TypeError(
                ConsoleMessage(
                    f"'{self._name}' must be of type {self._type.__name__}"
                ).error()
            )
        print(f"Setting {self._name} to {value}")
        instance.__dict__[self._name] = value


class Integer(Attribute):
    def __init__(
        self,
        nullable: bool = True,
        pk: bool = False,
    ) -> None:
        super().__init__(int, nullable, pk, sql_type="INTEGER")


class String(Attribute):
    def __init__(
        self,
        nullable: bool = True,
        pk: bool = False,
    ) -> None:
        super().__init__(str, nullable, pk, sql_type="TEXT")


class ManyToMany(Attribute):
    _entity: BaseORMEntity
    _attr: str
    _value: list[BaseORMEntity] = []

    def __init__(
        self,
        mapped_entity: Type[BaseORMEntity],
        mapped_attribute: str,
        nullable: bool = True,
        pk: bool = False,
    ) -> None:
        # Mapping as an integer, genereator then creates foreign key
        super().__init__(mapped_entity, nullable, pk, f"INTEGER")
        if not issubclass(mapped_entity, BaseORMEntity):
            raise ValueError(
                ConsoleMessage(
                    f"Mapped entity has to be sublass of BaseORMEntity."
                ).error()
            )
        self._entity = mapped_entity

    def __set__(
        self,
        instance,
        relations,
    ):
        if (relations is None or relations == []) and not self._nullable:
            raise ValueError(
                ConsoleMessage(f"'{self._name}' is not nullable.").error()
            )
        if relations is not None and not isinstance(relations, list):
            raise TypeError(
                ConsoleMessage(
                    f"'{self._name}' must be of type {list.__name__}"
                ).error()
            )
        if not all(issubclass(e.__class__, BaseORMEntity) for e in relations):
            raise TypeError(
                ConsoleMessage(
                    f"'{self._name}' has to only contain {self._type.__name__}"
                ).error()
            )
        print(f"Setting {self._name} to {relations}")
        instance.__dict__[self._name] = relations


class OneToMany(Attribute):
    pass


class ManyToOne(Attribute):
    pass
