
from __core__.application.use_cases import CreateCategoryUseCase, DeleteCategoryUseCase, GetCategoryUseCase, ListCategoriesUseCase, UpdateCategoryUseCase
from __core__.infra.repositories import CategoryRepositoryOrm


class ListCategoriesUseCaseFactory:

    @staticmethod
    def make() -> ListCategoriesUseCase:
        return ListCategoriesUseCase(
            CategoryRepositoryOrm()
        )


class GetCategoryUseCaseFactory:

    @staticmethod
    def make() -> GetCategoryUseCase:
        return GetCategoryUseCase(
            CategoryRepositoryOrm()
        )


class CreateCategoriesUseCaseFactory:

    @staticmethod
    def make() -> CreateCategoryUseCase:
        return CreateCategoryUseCase(
            CategoryRepositoryOrm()
        )


class UpdateCategoriesUseCaseFactory:

    @staticmethod
    def make() -> UpdateCategoryUseCase:
        return UpdateCategoryUseCase(
            CategoryRepositoryOrm()
        )


class DeleteCategoriesUseCaseFactory:

    @staticmethod
    def make() -> DeleteCategoryUseCase:
        return DeleteCategoryUseCase(
            CategoryRepositoryOrm()
        )
