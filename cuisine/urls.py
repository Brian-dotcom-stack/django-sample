from django.urls import path
from . import views

app_name = "cuisine"

urlpatterns = [
   # cuisine_list view as a class
   path('', views.CuisineListView.as_view(), name='cuisine_list_cls'),
   
   # Cuisine list view as a function
   #path('', views.Cuisine_list, name='Cuisine_list'),
   
   # food_detail view as a class
  # path('<slug:slug>', views.CuisineDetailView.as_view(), name='Cuisine_detail'),
   
   
   # Cuisine detail view as a functiion 
   path('<slug:cuisine>/', views.Cuisine_detail, name = 'Cuisine_detail'),
]

