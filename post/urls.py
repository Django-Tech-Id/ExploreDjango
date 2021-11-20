from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboardPost, name='dashboard-post'),
    path('edit/<id>', views.dashboardPostEdit, name='dashboard-post-edit'),
    path('create/', views.dashboardPostCreate, name='dashboard-post-create'),
    path('delete/<id>', views.dashboardPostDelete, name='dashboard-post-delete')
]