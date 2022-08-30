from django.contrib import admin
from imobile import consts as Consts
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

    @admin.display(
        description="Created_at",
    )
    def get_birthday_str(self):
        return self.birthday.strftime("%d/%m/%Y")

    @admin.display(
        description="Document",
    )
    def get_document_str(self):
        my_document = self.document
        document = "{}.{}.{}-{}".format(
            my_document[:3], my_document[3:6], my_document[6:9], my_document[9:]
        )
        return document

    @admin.display(
        description="Phone",
    )
    def get_phone_str(self):
        my_phone = self.phone
        if len(my_phone) == 11:
            return "({}) {} {}-{}".format(
                my_phone[:2], my_phone[2:3], my_phone[3:7], my_phone[7:11]
            )
        return self.phone

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

    owner = ForeignKey(Person, on_delete=DO_NOTHING, related_name="%(class)s_owner")

    @admin.display(
        description="Created_at",
    )
    def get_create_time_str(self):
        return self.created_at.strftime("%d/%m/%Y")

    @admin.display(
        description="Value",
    )
    def get_value_str(self):
        limit_value = round(self.value, Consts.MONETARY_DECIMAL_PLACES)
        return f"{Consts.MONETARY_PREFIX} {limit_value}"

    @admin.display(
        description="Comission",
    )
    def get_comission_str(self):
        limit_value = round(self.commision, Consts.MONETARY_DECIMAL_PLACES)
        return f"{limit_value} {Consts.MONETARY_PERCENT_SUFIX}"


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

    @admin.display(
        description="Value",
    )
    def get_value_str(self):
        limit_value = round(self.value, Consts.MONETARY_DECIMAL_PLACES)
        return f"{Consts.MONETARY_PREFIX} {limit_value}"

    @admin.display(
        description="Comission",
    )
    def get_comission_str(self):
        limit_value = round(self.commision, Consts.MONETARY_DECIMAL_PLACES)
        return f"{limit_value} {Consts.MONETARY_PERCENT_SUFIX}"
