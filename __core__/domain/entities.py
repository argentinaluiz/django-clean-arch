import abc
import uuid
from dataclasses import dataclass
from typing import Any
from __core__.domain.exceptions import NotImplementedException
from __core__.domain.validations import DomainValidation



class Entity(metaclass=abc.ABCMeta):
    def set(self, name: str, value: Any):
        object.__setattr__(self, name, value)
        return self

    def __post_init__(self):
        if(not self.id):
            self.set('id', uuid.uuid4())
        self.validate()
    
    @abc.abstractclassmethod
    def validate(self):
        raise NotImplementedException

# 3.7
@dataclass(frozen=True)
class Category(Entity):
    name: str
    description: str
    is_active: bool = True
    id: uuid.UUID = None

    def validate(self):
        DomainValidation.uuid('id', self.id)

        DomainValidation.not_null('name', self.name)
        DomainValidation.max_length('name', self.name, 255)

        DomainValidation.not_null('description', self.description)
        DomainValidation.max_length('description', self.description, 255)

        DomainValidation.not_null('is_active', self.is_active)


# __core__.domain
# infra