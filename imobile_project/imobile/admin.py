from django.contrib.admin import ModelAdmin, TabularInline
from django.contrib.admin import site as Site

from .models import Person, Property, Sale, Feature, Adress, PropertyFeature


class PersonAdmin(ModelAdmin):
    list_display = ("id", "name", "get_birthday_str", "get_document_str", "get_phone_str", "email")


class FeatureInline(TabularInline):
    model = PropertyFeature
    extra = 1


class AdressInline(TabularInline):
    model = Adress
    extra = 1


class PropertyAdmin(ModelAdmin):
    list_display = (
        "id",
        "owner",
        "code",
        "category",
        "get_comission_str",
        "get_value_str",
        "get_create_time_str",
        "status",
    )

    inlines = [FeatureInline, AdressInline]


class FeatureAdmin(ModelAdmin):
    list_display = ("id", "description", "type")


class SaleAdmin(ModelAdmin):
    list_display = ("id", "get_value_str", "get_comission_str", "buyer", "seller", "agent")


Site.register(Person, PersonAdmin)
Site.register(Property, PropertyAdmin)
Site.register(Sale, SaleAdmin)
Site.register(Feature, FeatureAdmin)
