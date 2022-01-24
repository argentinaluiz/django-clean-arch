

import abc
from typing import Any, List

from __core__.domain.exceptions import NotImplementedException
from .entities import Category


class CategoryRepositoryInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def find_all(self) -> List[Category]:
        raise NotImplementedException
    
    @abc.abstractmethod
    def find_by_id(self, id: str) -> Category:
        raise NotImplementedException
    
    @abc.abstractmethod
    def insert(self, entity: Any) -> Category:
        raise NotImplementedException
    
    @abc.abstractmethod
    def update(self, entity: Any) -> Category:
        raise NotImplementedException
    
    @abc.abstractmethod
    def delete(self, id: str) -> None:
        raise NotImplementedException
