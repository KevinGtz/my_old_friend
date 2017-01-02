#-*-encoding:utf-8-*-
from django.conf.urls import include, url
from django.contrib import admin
from tienda.views import * #importamos las vistas de la app tienda
from api import urls as api_urls

"""creamos una url para cada vista, aqui vamos a hacer un CRUD
    (Create, Read, Update, Delete), cada view tiene un template, checalo 
    en el directorio de templates, como te podras dar cuenta creamos un directorio
    para las urls de la app en este caso tienda"""
urlpatterns = [
    url(r'^$', TiendaListView.as_view(), name='home'),
    url(r'^new/', TiendaCreate.as_view(), name='create'),
    url(r'^detail/(?P<pk>[0-9]+)/$', TiendaDetail.as_view(), name='detail' ),
    url(r'^update/(?P<pk>[0-9]+)/$', TiendaUpdate.as_view(), name='update' ),
    url(r'^delete/(?P<pk>[0-9]+)/$', TiendaDelete.as_view(), name='delete' ),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(api_urls, namespace='api')),
]