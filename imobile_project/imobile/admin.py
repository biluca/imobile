from django.contrib.admin import ModelAdmin, TabularInline
from django.contrib.admin import site as Site

from .models import Person, Property, Sale, Feature, Adress, PropertyFeature


class PersonAdmin(ModelAdmin):
    list_display = ("id", "name", "birthday", "document", "phone", "email")


class FeatureInline(TabularInline):
    model = PropertyFeature
    extra = 1


class AdressInline(TabularInline):
    model = Adress
    extra = 1


class PropertyAdmin(ModelAdmin):
    list_display = (
        "id",
        "code",
        "category",
        "commision",
        "value",
        "created_at",
        "status",
    )

    inlines = [FeatureInline, AdressInline]


class FeatureAdmin(ModelAdmin):
    list_display = ("id", "description", "type")


class SaleAdmin(ModelAdmin):
    list_display = ("id", "value", "commision", "buyer", "seller", "agent")


Site.register(Person, PersonAdmin)
Site.register(Property, PropertyAdmin)
Site.register(Sale, SaleAdmin)
Site.register(Feature, FeatureAdmin)
