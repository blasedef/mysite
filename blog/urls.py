from django.conf.urls import url
from . import views

urlpatterns = [
	# post views
	url(r'^$', views.post_list, name='post_list'),
	url(r'^(?P<year>\d{4})/'\
		r'(?P<month>\d{2})/'\
		r'(?P<day>\d{2})/'\
		r'(?P<post>[-\w]+)/$',\
		views.post_detail, name='post_detail'),
]