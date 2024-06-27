from django.shortcuts import render, redirect
from django.views import View

from .forms import IngredientForm, CategoryForm, RecipeForm
from .models import Ingredient


# def all_receipt(request):
#     return render(request, 'cocktail/all_receipt.html')


class AddIngredientView(View):
    def get(self, request):
        form = IngredientForm()
        return render(request, 'cocktail/add_ingredient.html', {'form': form})

    def post(self, request):
        form = IngredientForm(request.POST, request.FILES)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.save()
            return redirect('recipes:ingredients_list')
        return render(request, 'cocktail/add_ingredient.html', {'form': form})


class AddCategoryView(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'cocktail/add_category.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('recipes:categories_list')
        return render(request, 'cocktail/add_category.html', {'form': form})


class AddRecipeView(View):
    def get(self, request):
        form = RecipeForm()
        return render(request, 'cocktail/add_recipe.html', {'form': form})

    def post(self, request):
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('recipes:recipes_list')
        return render(request, 'cocktail/add_recipe.html', {'form': form})
