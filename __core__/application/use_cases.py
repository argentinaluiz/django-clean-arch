from dataclasses import dataclass, asdict
from typing import List

from __core__.domain.repositories import CategoryRepositoryInterface
from __core__.domain.entities import Category

@dataclass(frozen=True)
class CategoryOutput:
    id: str
    name: str
    description: str
    is_active: bool


@dataclass(frozen=True)
class ListCategoriesOutput:
    categories: List[CategoryOutput]

class ListCategoriesUseCase:

    repository: CategoryRepositoryInterface

    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        categories = self.repository.find_all()
        return ListCategoriesOutput(
            categories=[CategoryOutput(**asdict(c)) for c in categories]
        )


@dataclass(frozen=True)
class GetCategoryInput:
    id: str


class GetCategoryUseCase:

    repository: CategoryRepositoryInterface

    def __init__(self, repository):
        self.repository = repository

    def execute(self, input: GetCategoryInput):
        category = self.repository.find_by_id(input.id)
        return CategoryOutput(**asdict(category))

@dataclass(frozen=True)
class CategoryInput:
    name: str
    description: str
    is_active: bool


@dataclass(frozen=True)
class CreateCategoryInput(CategoryInput):
    pass

class CreateCategoryUseCase:

    repository: CategoryRepositoryInterface

    def __init__(self, repository):
        self.repository = repository

    def execute(self, input: CreateCategoryInput):
        entity = Category(**asdict(input))
        category = self.repository.insert(entity)
        return CategoryOutput(**asdict(category))

@dataclass(frozen=True)
class UpdateCategoryInput:
    id: str
    category: CategoryInput

class UpdateCategoryUseCase:

    repository: CategoryRepositoryInterface

    def __init__(self, repository):
        self.repository = repository

    def execute(self, input: UpdateCategoryInput):
        entity = Category(
            id=input.id,
            **asdict(input.category)
        )
        category = self.repository.update(entity)
        return CategoryOutput(**asdict(category))

@dataclass(frozen=True)
class DeleteCategoryInput:
    id: str

class DeleteCategoryUseCase:

    repository: CategoryRepositoryInterface

    def __init__(self, repository):
        self.repository = repository

    def execute(self, input: DeleteCategoryInput) -> None:
        self.repository.delete(input.id)
