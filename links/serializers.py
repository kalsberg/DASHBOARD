# Direct Import
import re

# Relative Imports
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin
from DASHBOARD.settings import MEDIA_URL

# Project Imports
from .models import HeaderLink, Category, SubCategory, Link, ContactInformation, FooterLink


class HeaderLinkSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = HeaderLink
        fields = '__all__'


class CategorySerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    sub_category_name = serializers.ReadOnlyField(source='name')
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category',
                                                     write_only=True, required=False)

    class Meta:
        model = SubCategory
        fields = '__all__'


class LinkSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    sub_category = SubCategorySerializer(read_only=True)
    sub_category_id = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all(), source='sub_category',
                                                         write_only=True, required=False)
    category_name = serializers.ReadOnlyField(source='sub_category.category.name')

    def to_representation(self, instance):
        data = super(LinkSerializer, self).to_representation(instance)
        data['icon'] = "http://{0}{1}categories/{2}.svg".format(self.context.get("request").get_host(),
                                                                MEDIA_URL, data['category_name'].strip().lower())
        return data

    class Meta:
        model = Link
        fields = '__all__'


class ContactInformationSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = '__all__'


class FooterLinkSerializer(FriendlyErrorMessagesMixin, serializers.ModelSerializer):
    class Meta:
        model = FooterLink
        fields = '__all__'