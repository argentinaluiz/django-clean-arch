from dataclasses import asdict
from typing import List

from __core__.domain.entities import Category
from __core__.domain.exceptions import EntityNotFoundException
from __core__.domain.repositories import CategoryRepositoryInterface
from app.models import CategoryOrm
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict


class CategoryRepositoryOrm(CategoryRepositoryInterface):

    def find_all(self) -> List[Category]:
        categories = CategoryOrm.objects.values()
        return [Category(**c) for c in categories]

    def insert(self, entity: Category) -> Category:
        model = CategoryOrm.objects.create(**asdict(entity))
        return Category(**model_to_dict(model))
    
    def update(self, entity: Category) -> Category:
        self.find_by_id(entity.id)
        model = CategoryOrm(**asdict(entity))
        model.save(force_update=True)
        return Category(**model_to_dict(model))
    
    def delete(self, id: str) -> None:
        model = self.__get(id)
        model.delete()
    
    def find_by_id(self, id: str) -> Category:
        try:
            category = self.__get(id)
            return Category(**model_to_dict(category))
        except ObjectDoesNotExist as e:
            raise EntityNotFoundException(
                "Category not found using ID %s" % id
            )
    
    def __get(self, id: str) -> CategoryOrm:
        try:
            return CategoryOrm.objects.get(id=id)
        except ObjectDoesNotExist as e:
            raise EntityNotFoundException(
                "Category not found using ID %s" % id
            )