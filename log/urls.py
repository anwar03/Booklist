from django.conf.urls import url , include
from django.contrib.auth.views import  login
#from django.contrib.auth.decorators import login_required

from log.views import logout_page, register_page, main_page, detail, post


urlpatterns = [
    url(r'^booklist/(?P<book_id>[0-9]+)/$', detail, name='detail'),
    url(r'^post/$', post),
    #url(r'^post/$', login_required(post)),
	url(r'^login/$', login, name='login'),
	url(r'^logout$', logout_page),
	url(r'^register/$', register_page),
    url(r'^$', main_page, name='home'),
]