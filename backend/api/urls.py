from django.urls import path
from .views import UserView

urlpatterns = [
    path('user/', view=UserView.as_view()),
    path('user/<str:user>/', view=UserView.as_view())
]
