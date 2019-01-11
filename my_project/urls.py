from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from tutorial.views import tickets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='base.html'), name='base'),
    path('tickets/', tickets),
    path('iprestrict/', include('iprestrict.urls', namespace='iprestrict')),
]
