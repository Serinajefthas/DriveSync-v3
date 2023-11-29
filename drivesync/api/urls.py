from django.urls import path, include
from .views import UserView, CreateUserView

#extensions after api/, redirected from urls.py 
urlpatterns = [
    path('home', UserView.as_view()), #.../api/home
    path('user', UserView.as_view()),
    path('create-user', CreateUserView.as_view()),
    path('', include('frontend.urls'))
]