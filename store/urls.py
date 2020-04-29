from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.allProdcat, name='allProdcat'),
    path('<slug:c_slug>/', views.allProdcat, name='proucts_by_category'),
]
