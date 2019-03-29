from collector import views
from django.conf.urls import url

app_name='collector'

urlpatterns = [
    url('', views.index, name='index')
]
