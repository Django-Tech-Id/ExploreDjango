from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboardComment, name='dashboard-comment'),
    path('edit/<id>', views.dashboardCommentEdit, name='dashboard-comment-edit'),
    path('create/', views.dashboardCommentCreate, name='dashboard-comment-create'),
    path('delete/<id>', views.dashboardCommentDelete, name='dashboard-comment-delete')
]