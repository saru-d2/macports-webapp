"""MacPorts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from ports import views

urlpatterns = [
    path('', views.index, name='home'),
    path('statistics/submit/', views.stats_submit, name='stats_submit'),
    path('statistics/ports/', views.stats_port_installations, name='stats_port_installations'),
    path('statistics/ports/filter/', views.stats_port_installations_filter, name='stats_port_installations_filter'),
    path('statistics/faq/', views.stats_faq, name='stats_faq'),
    path('statistics/', views.stats, name='stats_home'),
    url(r'^maintainer/github/(?P<github_handle>[-a-zA-Z0-9_.]+)/$', views.maintainer_detail_github, name='maintainer_detail_github'),
    url(r'^maintainer/email/(?P<name>[-a-zA-Z0-9_.]+)__(?P<domain>[-a-zA-Z0-9_.]+)/$', views.maintainer_detail_email, name='maintainer_detail_email'),
    path('port/', include('ports.urls'), name='port-index'),
    path('ports/', views.index, name='ports-index'),
    path('ports/search/', views.search, name='ports_search'),
    path('ports/filter/maintainer/', views.search_ports_in_maintainer, name='search_ports_in_maintainer'),
    path('ports/filter/category/', views.search_ports_in_category, name='search_ports_in_category'),
    path('ports/filter/variant/', views.search_ports_in_variant, name='search_ports_in_variant'),
    path('ports/load_tickets/', views.tickets, name='trac_tickets'),
    path('ports/category/<slug:cat>/', views.categorylist, name='category_list'),
    url(r'^ports/variant/(?P<variant>[a-zA-Z0-9_.]+)/$', views.variantlist, name='variant_list'),
    path('ports/all_builds/filter/', views.all_builds_filter, name='all_builds_filter'),
    path('ports/all_builds/', views.all_builds_view, name='all_builds'),
    path('api/v1/', include('api_v1.urls')),
    path('about/', views.about_page, name='about_page'),
]
