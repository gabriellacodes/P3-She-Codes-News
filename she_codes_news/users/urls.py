from django.urls import path
# need to import the views here in order for the urlpatterns to work
from .views import CreateAccountView
from .views import DetailAccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('user-page/<str:slug>/', DetailAccountView.as_view(), name='userPage'),
    path('user-page/', DetailAccountView.as_view(), name='userPage'),
]