from datetime import date

from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Prefecture(models.Model):
    name = models.CharField("Оф. Краткое наименование префектуры", max_length=255)

    def __str__(self):
        return self.name

class Operating_organizations(models.Model):
    name = models.CharField("Эксплуатирующие организации", max_length=255)

    def __str__(self):
        return self.name

class Shelter(models.Model):
    name = models.CharField("Оф. Краткое наименование приюта", max_length=255)
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    address = models.CharField("Адрес приюта", max_length=255)
    phone = models.CharField("Телефон приюта", max_length=255, null=True)

    def __str__(self):
        return self.name


class Reason_retirement(models.Model):
    reason_retirement = models.CharField("причина выбытия", max_length=255)

    def __str__(self):
        return self.reason_retirement


class Reason_death(models.Model):
    reason_death = models.CharField("причина смерти", max_length=255)

    def __str__(self):
        return self.reason_death


class Reason_euthanasia(models.Model):
    reason_euthanasia = models.CharField("причина эвтаназии", max_length=255)

    def __str__(self):
        return self.reason_euthanasia


class District(models.Model):
    district = models.CharField("административный округ", max_length=255)

    def __str__(self):
        return self.district


class Size(models.Model):
    size = models.CharField("размер", max_length=255)

    def __str__(self):
        return self.size


class Tail(models.Model):
    tail = models.CharField("хвост", max_length=255)

    def __str__(self):
        return self.tail


class Ears(models.Model):
    ears = models.CharField("уши", max_length=255)

    def __str__(self):
        return self.ears


class Wool(models.Model):
    wool = models.CharField("шерсть", max_length=255)

    def __str__(self):
        return self.wool


class Color(models.Model):
    color = models.CharField("окрас", max_length=255)

    def __str__(self):
        return self.color


class Breed(models.Model):
    breed = models.CharField("порода", max_length=255)

    def __str__(self):
        return self.breed


class Sex(models.Model):
    sex = models.CharField("пол", max_length=255)

    def __str__(self):
        return self.sex


class Kind(models.Model):
    kind = models.CharField("вид", max_length=255)

    def __str__(self):
        return self.kind


class Pet(models.Model):
    # общие  сведения
    ids = models.CharField("карточка учета животного №", max_length=255)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE)
    age = models.IntegerField("возраст, год")
    weight = models.IntegerField("вес, кг")
    name = models.CharField("кличка", max_length=255)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    wool = models.ForeignKey(Wool, on_delete=models.CASCADE)
    ears = models.ForeignKey(Ears, on_delete=models.CASCADE)
    tail = models.ForeignKey(Tail, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    # дополнительные сведения
    special_signs = models.CharField("особые приметы", max_length=255)
    aviary = models.IntegerField("Вольер №")
    identification_mark = models.BigIntegerField("идентификационная метка", null=True)
    sterilization_date = models.CharField("дата стерилизации", max_length=255, null=True)
    name_veterinarian = models.CharField("ф.и.о. ветеринарного врача", max_length=255, null=True)
    socialized = models.BooleanField("Социализировано (да/нет)", default=False)
    # сведения об отлове
    work_order = models.CharField("заказ-наряд / акт о поступлении животного №", max_length=255, null=True)
    work_order_date = models.DateField("заказ-наряд дата/ акт о поступлении животного, дата", null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    catch_report = models.CharField("акт отлова №", max_length=255, null=True)
    catching_address = models.CharField("адрес места отлова", max_length=255, null=True)
    # сведения о новых владельцах
    entity = models.CharField("юридическое лицо ", max_length=255, null=True)
    name_guardians = models.CharField("ф.и.о. опекунов", max_length=255, null=True)
    natural_person_name = models.CharField("физическое лицо ф.и.о.", max_length=255, null=True)
    # движение животного
    date_to_shelter = models.CharField("дата поступления в приют", max_length=255, null=True)
    act_no = models.CharField("акт №", max_length=255, null=True)
    date_leaving_shelter = models.CharField("дата выбытия из приюта", max_length=255, null=True)
    reason_retirement = models.ForeignKey(Reason_retirement, on_delete=models.CASCADE, null=True)
    reason_death = models.ForeignKey(Reason_death, on_delete=models.CASCADE, null=True)
    reason_euthanasia = models.ForeignKey(Reason_euthanasia, on_delete=models.CASCADE, null=True)
    act_retirement = models.CharField("акт/договор №", max_length=255, null=True)
    # ответственные за животное
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    operating_organizations = models.ForeignKey(Operating_organizations, on_delete=models.CASCADE)
    name_leader_shelter = models.CharField("ф.и.о. руководителя приюта", max_length=255)
    name_care_worker = models.CharField("ф.и.о. сотрудника по уходу за животным", max_length=255)

    def __str__(self):
        return self.name


class Processing_parasites(models.Model):
    no = models.IntegerField("№ п/п")
    date = models.DateField("дата")
    drug_name = models.CharField("название препарата", max_length=255)
    dose = models.CharField("доза", max_length=255)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return self.drug_name+self.dose


class Vaccination_information(models.Model):
    no = models.IntegerField("№ п/п")
    date = models.DateField("дата")
    type_vaccine = models.CharField("вид вакцины", max_length=255)
    series = models.CharField("№ серии", max_length=255)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return self.type_vaccine+self.series


class Health_information(models.Model):
    date = models.DateField("дата")
    anamnesis = models.CharField("анамнез", max_length=255)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return self.anamnesis
