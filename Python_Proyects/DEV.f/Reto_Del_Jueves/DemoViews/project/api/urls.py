from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^tienda/$', views.TiendaView.as_view(), name='tienda_api'),
    url(r'^tienda/(?P<contacto>[-\w]+)/$', views.TiendaView.as_view(), name='tienda_api'),
    url(r'^tienda/(?P<pk>[0-9]+)/$', views.TiendaDetailView.as_view(), name='tienda_detalle_api'),
    url(r'^producto/$', views.ProductoCreate.as_view(), name='producto_api'),
]