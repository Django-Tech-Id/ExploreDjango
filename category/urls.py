from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboardCategory, name='dashboard-category'),
    path('edit/<id>', views.dashboardCategoryEdit, name='dashboard-category-edit'),
    path('create/', views.dashboardCategoryCreate, name='dashboard-category-create'),
    path('delete/<id>', views.dashboardCategoryDelete, name='dashboard-category-delete')
]