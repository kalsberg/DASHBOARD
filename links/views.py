# Relative Imports
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_bulk import ListBulkCreateUpdateAPIView

# Project Imports
from .models import HeaderLink, Category, SubCategory, Link, ContactInformation, FooterLink
from .serializers import HeaderLinkSerializer, CategorySerializer, SubCategorySerializer, LinkSerializer, \
    ContactInformationSerializer, FooterLinkSerializer


class HeaderLinksList(generics.ListCreateAPIView):
    queryset = HeaderLink.objects.all()
    serializer_class = HeaderLinkSerializer


class HeaderLinksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HeaderLink.objects.all()
    serializer_class = HeaderLinkSerializer


class LinksList(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class LinksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class ContactInformationList(generics.ListCreateAPIView):
    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationSerializer


class ContactInformationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationSerializer


class FooterLinksList(generics.ListCreateAPIView):
    queryset = FooterLink.objects.all()
    serializer_class = FooterLinkSerializer


class FooterLinksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FooterLink.objects.all()
    serializer_class = FooterLinkSerializer