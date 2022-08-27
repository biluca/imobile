from sqlite3 import DateFromTicks
from django.db.models import (
    Model,
    CharField,
    DateField,
    DateTimeField,
    DecimalField,
    ForeignKey,
)
from django.db.models import DO_NOTHING


class Person(Model):
    class Meta:
        verbose_name_plural = "Persons"

    name = CharField(max_length=250)
    document = CharField(max_length=50)
    birthday = DateField()
    phone = CharField(max_length=50)
    email = CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Feature(Model):
    class Meta:
        verbose_name_plural = "Features"

    description = CharField(max_length=250)
    type = CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.description}"


class Property(Model):
    class Meta:
        verbose_name_plural = "Properties"

    code = CharField(max_length=50)
    category = CharField(max_length=50)
    status = CharField(max_length=50)
    created_at = DateTimeField()
    value = DecimalField(max_digits=99999, decimal_places=4)
    commision = DecimalField(max_digits=100, decimal_places=4)

    owner = ForeignKey(Person, on_delete=DO_NOTHING)


class Adress(Model):
    class Meta:
        verbose_name_plural = "Adresses"

    addres = CharField(max_length=250)
    number = CharField(max_length=15)
    locality = CharField(max_length=250)
    zipcode = CharField(max_length=15)
    complement = CharField(max_length=250)

    property = ForeignKey(Property, on_delete=DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.addres}, {self.number}, {self.locality}, {self.zipcode}"


class PropertyFeature(Model):
    property = ForeignKey(Property, on_delete=DO_NOTHING)
    feature = ForeignKey(Feature, on_delete=DO_NOTHING)
    value = CharField(max_length=150)


class Sale(Model):
    class Meta:
        verbose_name_plural = "Sales"

    value = DecimalField(max_digits=99999, decimal_places=4)
    commision = DecimalField(max_digits=100, decimal_places=4)

    seller = ForeignKey(Person, on_delete=DO_NOTHING, related_name="%(class)s_seller")
    buyer = ForeignKey(Person, on_delete=DO_NOTHING, related_name="%(class)s_buyer")
    agent = ForeignKey(Person, on_delete=DO_NOTHING, related_name="%(class)s_agent")
    property = ForeignKey(Property, on_delete=DO_NOTHING, related_name="property")
