from .._entity import Attribute, ManyToMany
from .._entity import BaseORMEntity
from .._io import ConsoleMessage
from typing import Type
from enum import Enum

class EntityManager:
    _changes: list[BaseORMEntity]

    def persist(self, e: Type[BaseORMEntity]) -> int:
        if not issubclass(e, BaseORMEntity):
            raise TypeError()
        self._changes.append(e)

    def delete(self, e: BaseORMEntity) -> int:
        pass

    def flush(self) -> int:
        pass
