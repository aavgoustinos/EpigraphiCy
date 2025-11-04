from django.urls import path
from .import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

urlpatterns = [

    path('', views.homepage, name="homepage"),
    path('place/<int:monument_id>/', views.monument_detail, name='monument_detail'),
    path('places/', views.monument_list, name='monument_list'),
    path('place/epigraphy/<int:epigraphy_id>/', views.epigraphy_detail, name='epigraphy_detail'),
    path('base/', views.base, name='base'),
    path('about/', about_view, name='about'),
    path('team/', team_view, name='team'),
    path('platform/', platform_view, name='platform'),

  

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
