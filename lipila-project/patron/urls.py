from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from business.views import CreateProductView, EditProductView, DeleteProductView

urlpatterns = [
     # Public URLS
     path('', views.index, name='index'),
     path('<str:user>/contribute', views.contribute, name='contribute'),

     path('creators/', views.list_creators, name='creators'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)