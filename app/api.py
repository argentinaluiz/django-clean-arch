from django.http import JsonResponse
from __core__.application.use_cases import (
    CategoryInput, 
    CreateCategoryInput, 
    DeleteCategoryInput, 
    GetCategoryInput, 
    UpdateCategoryInput
)
from __core__.infra.use_cases_factories import (
    CreateCategoriesUseCaseFactory, 
    DeleteCategoriesUseCaseFactory, 
    GetCategoryUseCaseFactory, 
    ListCategoriesUseCaseFactory, 
    UpdateCategoriesUseCaseFactory
)
from rest_framework import serializers, status, viewsets
from rest_framework.response import Response

class CategoryPresenter(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()

class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        output = ListCategoriesUseCaseFactory.make().execute()
        serializer = CategoryPresenter(output.categories, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, pk):
        output = GetCategoryUseCaseFactory.make().execute(
            GetCategoryInput(pk)
        )
        serializer = CategoryPresenter(output)
        return JsonResponse(serializer.data, safe=False)

    def create(self, request):
        output = CreateCategoriesUseCaseFactory.make().execute(
            CreateCategoryInput(**request.data)
        )
        serializer = CategoryPresenter(output)
        return JsonResponse(serializer.data, safe=False)

    def update(self, request, pk):
        output = UpdateCategoriesUseCaseFactory.make().execute(
            UpdateCategoryInput(
                id=pk,
                category=CategoryInput(**request.data)
            )
        )
        serializer = CategoryPresenter(output)
        return JsonResponse(serializer.data, safe=False)

    def destroy(self, request, pk):
        DeleteCategoriesUseCaseFactory.make().execute(
            DeleteCategoryInput(id=pk)
        )
        return Response(status=status.HTTP_204_NO_CONTENT)
