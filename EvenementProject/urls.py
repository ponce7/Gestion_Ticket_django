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
from django.urls import path,include
from accounts.views import signup, connexion, deconnexion
from events.views import edit, show_event, delete, newsletter, subscribe, SearchResultsView, generateQrCode,index, add_event, commande, pdf
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', connexion, name="connexion"),
    path('accounts/logout/', deconnexion, name="deconnexion"),
    path('accounts/signup/', signup, name="signup"),
    # path('modification/', modification, name="modification"),
    path('index/', index, name="index"),
    path('add_event/<int:id>/', add_event, name="add_event"),
    path('show_event/<int:id>/', show_event, name="show_event"),
    path('pdf/', pdf, name="pdf"),
    path('delete/<int:id>/supprimer/', delete, name="delete"),
    # path('', HomePageView.as_view(), name="home"),
    path('search/', SearchResultsView.as_view(), name="search_results"),
    path("newsletter", newsletter, name="newsletter"),
    path('commande/<int:id>/', commande, name="commande"),
    path('subscribe/', subscribe, name='subscribe'),
    path('edit/<int:id>/', edit, name="show_edit"),
    # path('page_convert/<int:id>/', render_pdf_view, name='render_pdf_view')
    # path('home/', generateQrCode, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
