from collector import views
from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

app_name = 'collector'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recorder/$', views.recorder, name='recorder'),
    url(r'^signin/$', LoginView.as_view(template_name='signin.html'), name="signin"),
    # url('signin/', login, {'template_name': 'signin.html'}, name='signin'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signout/$', views.signout, name='signout')
]
