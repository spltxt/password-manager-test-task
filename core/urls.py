from django.urls import path
from .views import AccountView, CreateAccount, DeleteAccount, EditAccount, ViewAccount

urlpatterns = [
    path('', AccountView, name='accounts'),
    path('create-account/', CreateAccount, name='create-account'),
    path('accounts/<str:pk>/', ViewAccount, name='account-details'),
    path('edit-account/<str:pk>/', EditAccount, name='edit-account'),
    path('delete-account/<str:pk>/', DeleteAccount, name='delete-account'),
]
