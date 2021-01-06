# Relative Imports
from django.db import models
from django.contrib.auth.models import User


class HeaderLink(models.Model):
    name = models.CharField(max_length=250, unique=True)
    link = models.CharField(max_length=1000)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Header Links"


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    icon = models.FileField(upload_to='categories')

    class Meta:
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    icon = models.FileField(upload_to='sub_categories')

    class Meta:
        unique_together = ('name', 'category')
        verbose_name_plural = "Sub-categories"


class Link(models.Model):
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=1000)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        unique_together = ('name', 'sub_category')
        verbose_name_plural = "Content Links"


class ContactInformation(models.Model):
    escalation_level = models.PositiveSmallIntegerField(max_length=2)
    personell = models.CharField(max_length=250, unique=True)
    phone_number = models.CharField(max_length=250)
    email = models.CharField(max_length=250, null=True)

    def __unicode__(self):
        return str(self.personell)

    class Meta:
        verbose_name_plural = "Contact Information"


class FooterLink(models.Model):
    name = models.CharField(max_length=250, unique=True)
    link = models.CharField(max_length=1000)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Footer Links"