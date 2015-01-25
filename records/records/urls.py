from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from patient import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'records.views.home', name='home'),
    # url(r'^records/', include('records.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name="home"),
    url(r'^register/$',(views.RegisterUser.as_view())),
    url(r'^records/$',(views.UserListView.as_view())),
    url(r'^search/$','patient.views.search'),
    url(r'^individual/(?P<pk>\d+)/$','patient.views.patient_detail', name="individual"),
    url(r'^save_disease/(?P<pk>\d+)/$', 'patient.views.patient_disease'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
