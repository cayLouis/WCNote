from django.conf.urls import url
from django.urls import include
from . import views

urlpatterns = [
    r'/connect', include(views.connect)
]
