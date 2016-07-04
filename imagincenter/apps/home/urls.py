from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [ 
	url(r'^$', Home.as_view(), name='home'),
	url(r'^nosotros$', About.as_view(), name='about'),
	url(r'^servicios$', Services.as_view(), name='services'),
	url(r'^servicio$', Service.as_view(), name='service'),
	url(r'^paciente$', Patient.as_view(), name='pacient'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)