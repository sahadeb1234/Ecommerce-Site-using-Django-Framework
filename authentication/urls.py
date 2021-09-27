from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.createUser,name="register"),
    path('verify/',views.verifyUser,name="verify"),
    path('login/',views.login_function,name="login"),
    path('your_account/',views.success,name="your_account"),
    path('logout/',views.logout_function,name='logout'),
    
]

