from django.conf.urls import url
from views import contact, home

urlpatterns = [
    url(r'^home/contact/$', view=contact),
    url(r'^home/$', view=home),
    url(r'^$', view=home),
]