from django.urls import path
from .import views

urlpatterns = [
    path('', views.home , name='home'),
    path('create/', views.create , name='create'),
    #path('create_api/', views.create_api , name='create_api'),
    path('transfer/',views.transfer , name='transfer'),
    # path('transfer_api/',views.transfer_api, name='transfer_api'),
    path('account_list/',views.accountlist, name='account_list'),
    path('account_detail/<str:pk>/',views.AccountDetail, name='account_detail'),
    path('account_create/',views.AccountCreate, name='account_create'),

    
    
]
