from rest_framework import serializers
import uuid

from .models import *
# Create your models here.


class PrefectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prefecture
        fields = ('id', 'name')

class Operating_organizationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operating_organizations
        fields = ('id', 'name')

class ShelterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shelter
        fields = ('id', 'name', 'prefecture', 'address', 'phone')

class Reason_retirementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reason_retirement
        fields = ('id', 'reason_retirement')

class Reason_deathSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reason_death
        fields = ('id', 'reason_death')

class Reason_euthanasiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reason_euthanasia
        fields = ('id', 'reason_euthanasia')

class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = ('id', 'district')

class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = ('id', 'size')

class TailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tail
        fields = ('id', 'tail')

class EarsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ears
        fields = ('id', 'ears')

class WoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wool
        fields = ('id', 'wool')

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ('id', 'color')

class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = ('id', 'breed')

class KindSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kind
        fields = ('id', 'kind')

class SexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sex
        fields = ('id', 'sex')

class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ('id',
                  'ids',
                  'kind',
                  'age',
                  'weight',
                  'name',
                  'sex',
                  'breed',
                  'color',
                  'wool',
                  'ears',
                  'tail',
                  'size',
                  'special_signs',
                  'aviary',
                  'identification_mark',
                  'sterilization_date',
                  'name_veterinarian',
                  'socialized',
                  'work_order',
                  'work_order_date',
                  'district',
                  'catch_report',
                  'catching_address',
                  'entity',
                  'name_guardians',
                  'natural_person_name',
                  'date_to_shelter',
                  'act_no',
                  'date_leaving_shelter',
                  'reason_retirement',
                  'reason_death',
                  'reason_euthanasia',
                  'act_retirement',
                  'shelter',
                  'operating_organizations',
                  'name_leader_shelter',
                  'name_care_worker')

class Processing_parasites(serializers.ModelSerializer):

    class Meta:
        model = Processing_parasites
        fields = ('id', 'no', 'date', 'drug_name', 'dose', 'pet')

class Vaccination_informationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vaccination_information
        fields = ('id', 'no', 'date', 'type_vaccine', 'series', 'pet')

class Health_informationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Health_information
        fields = ('id', 'date', 'anamnesis', 'pet')

