from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_test, name='create_test'),
    path('test/<int:test_id>/', views.view_test, name='view_test'),
    path('test/<int:test_id>/add_variant/', views.add_variant, name='add_variant'),
    path('test/int:test_id/add_outcome/', views.add_outcome, name='add_outcome'),
]
