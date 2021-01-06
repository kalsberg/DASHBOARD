from django.conf.urls import url
import views

urlpatterns = [
    url(r'^header_links/$', views.HeaderLinksList.as_view()),
    url(r'^header_links/(?P<pk>[0-9]+)/$', views.HeaderLinksDetail.as_view()),

    url(r'^links/$', views.LinksList.as_view()),
    url(r'^links/(?P<pk>[0-9]+)/$', views.LinksDetail.as_view()),

    url(r'^contact_info/$', views.ContactInformationList.as_view()),
    url(r'^contact_info/(?P<pk>[0-9]+)/$', views.ContactInformationDetail.as_view()),

    url(r'^footer_links/$', views.FooterLinksList.as_view()),
    url(r'^footer_links/(?P<pk>[0-9]+)/$', views.FooterLinksDetail.as_view()),
]
