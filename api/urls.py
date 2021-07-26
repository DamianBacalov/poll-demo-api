from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from . import views


schema_view = get_swagger_view(title='KuberVoter')

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^api/option/$', views.get_all_options, name="get_all_options"),
    url(r'^api/option/new/$', views.create_option, name="create_option"),
    url(r'^api/option/(?P<option_id>[0-9]*)/$', views.get_option, name="get_option"),
    url(r'^api/option/(?P<option_id>[0-9]*)/vote/$', views.vote_option, name="vote_option"),
    url(r'^api/option/(?P<option_id>[0-9]*)/reset/$', views.reset_option, name="reset_option"),
    url(r'^api/visit/$', views.register_visit, name="register_visit")
]

