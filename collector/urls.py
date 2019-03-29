from collector import views
from django.conf.urls import url
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

app_name='collector'

urlpatterns = [
    url('', views.index, name='index'),
    # url('signin/', login, {'template_name': 'signin.html'}, name='signin'),
    # url('signup/', views.signup, name='signup'),
    # url('signout/', views.signout, name='signout')
# url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name="login"),
]
