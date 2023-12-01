"""
URL configuration for EvenementProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import signup, login
from events.views import index, add_event, cart, commande

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup"),
    path('index/', index, name="index"),
    path('event/', add_event, name="add_event"),
    path('cart/', cart, name="cart"),
    # path('event/<str:slug>/add-to-cart/', add_to_cart, name="add_to_cart"),
    path('commande/<str:slug>/', commande, name="commande")
]
