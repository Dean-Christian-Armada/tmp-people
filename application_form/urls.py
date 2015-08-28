from django.conf.urls import include, url

from . import views

urlpatterns = [
	# url(r'^$', views.form, name='application_form' ),
	url(r'^tmp$', views.tmp_form, name='application_form' ),
	url(r'^tmp-image/$', views.tmp_image, name='tmp_image'),
	url(r'^success/$', views.success, name='success'),
	# url(r'^pdf-report/$', views.pdf_report, name='pdf_report'),
	url(r'^pdf-report/(?P<id>[0-9]*)/$', views.pdf_report, name='pdf_report'),
	# url(r'^pdf-report/(?P<id>[0-9]*)/(?P<template>[\w\-]*)/$', views.pdf_report, name='pdf_report'),
]