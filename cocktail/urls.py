from django.urls import path

from cocktail import views
from .views import AddIngredientView, AddCategoryView, AddRecipeView

app_name = 'cocktail'

urlpatterns = [
    path('categories/add/', AddCategoryView.as_view(), name='add_category'),
    path('ingredients/add/', AddIngredientView.as_view(), name='add_ingredient'),
    path('recipes/add/', AddRecipeView.as_view(), name='add_recipe'),
]
