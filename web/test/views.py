import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

from .models import *
from .serializers import *


# Prefecture
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_prefecture(request):
    try:
        prefecture = Prefecture.objects.filter(**request.query_params)
        serializer = PrefectureSerializer(prefecture, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_prefecture(request):
    try:
        prefecture = Prefecture.objects.create(**request.query_params)
        serializer = PrefectureSerializer(prefecture)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_prefecture(request, pk):
    try:
        prefecture = Prefecture.objects.filter(pk=pk)
        prefecture.update(**request.query_params)
        prefecture = Prefecture.objects.get(pk=pk)
        serializer = PrefectureSerializer(prefecture)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_prefecture(request, pk):
    try:
        prefecture = Prefecture.objects.get(pk=pk)
        prefecture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Operating_organizations
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_operating_organizations(request):
    try:
        operating_organizations = Operating_organizations.objects.filter(**request.query_params)
        serializer = Operating_organizationsSerializer(operating_organizations, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_operating_organizations(request):
    try:
        operating_organizations = Operating_organizations.objects.create(**request.query_params)
        serializer = Operating_organizationsSerializer(operating_organizations)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_operating_organizations(request, pk):
    try:
        operating_organizations = Operating_organizations.objects.filter(pk=pk)
        operating_organizations.update(**request.query_params)
        operating_organizations = Operating_organizations.objects.get(pk=pk)
        serializer = Operating_organizationsSerializer(operating_organizations)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_operating_organizations(request, pk):
    try:
        operating_organizations = Operating_organizations.objects.get(pk=pk)
        operating_organizations.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Shelter
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_shelter(request):
    try:
        shelter = Shelter.objects.filter(**request.query_params)
        serializer = ShelterSerializer(shelter, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_shelter(request):
    try:
        shelter = Shelter()
        shelter.prefecture = Prefecture.objects.get(pk=int(request.query_params['prefecture_id']))
        shelter.name = request.query_params['name']
        shelter.address = request.query_params['address']
        shelter.phone = request.query_params['phone']
        shelter.save()
        serializer = ShelterSerializer(shelter)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_shelter(request, pk):
    try:
        shelter = Shelter.objects.filter(pk=pk)
        if 'prefecture' in request.query_params:
            shelter.prefecture = Prefecture.objects.get(pk=int(request.query_params['prefecture_id']))
        if 'name' in request.query_params:
            shelter.name = request.query_params['name']
        if 'address' in request.query_params:
            shelter.address = request.query_params['address']
        if 'phone' in request.query_params:
            shelter.phone = request.query_params['phone']
        shelter.save()
        shelter = Shelter.objects.get(pk=pk)
        serializer = ShelterSerializer(shelter)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_shelter(request, pk):
    try:
        shelter = Shelter.objects.get(pk=pk)
        shelter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Reason_retirement
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_reason_retirement(request):
    try:
        reason_retirement = Reason_retirement.objects.filter(**request.query_params)
        serializer = Reason_retirementSerializer(reason_retirement, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_reason_retirement(request):
    try:
        reason_retirement = Reason_retirement.objects.create(**request.query_params)
        serializer = Reason_retirementSerializer(reason_retirement)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_reason_retirement(request, pk):
    try:
        reason_retirement = Reason_retirement.objects.filter(pk=pk)
        reason_retirement.update(**request.query_params)
        reason_retirement = Reason_retirement.objects.get(pk=pk)
        serializer = Reason_retirementSerializer(reason_retirement)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_reason_retirement(request, pk):
    try:
        reason_retirement = Reason_retirement.objects.get(pk=pk)
        reason_retirement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Reason_death
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_reason_death(request):
    try:
        reason_death = Reason_death.objects.filter(**request.query_params)
        serializer = Reason_deathSerializer(reason_death, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_reason_death(request):
    try:
        reason_death = Reason_death.objects.create(**request.query_params)
        serializer = Reason_deathSerializer(reason_death)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_reason_death(request, pk):
    try:
        reason_death = Reason_death.objects.filter(pk=pk)
        reason_death.update(**request.query_params)
        reason_death = Reason_death.objects.get(pk=pk)
        serializer = Reason_deathSerializer(reason_death)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_reason_death(request, pk):
    try:
        reason_death = Reason_death.objects.get(pk=pk)
        reason_death.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Reason_euthanasia
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_reason_euthanasia(request):
    try:
        reason_euthanasia = Reason_euthanasia.objects.filter(**request.query_params)
        serializer = Reason_euthanasiaSerializer(reason_euthanasia, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_reason_euthanasia(request):
    try:
        reason_euthanasia = Reason_euthanasia.objects.create(**request.query_params)
        serializer = Reason_euthanasiaSerializer(reason_euthanasia)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_reason_euthanasia(request, pk):
    try:
        reason_euthanasia = Reason_euthanasia.objects.filter(pk=pk)
        reason_euthanasia.update(**request.query_params)
        reason_euthanasia = Reason_euthanasia.objects.get(pk=pk)
        serializer = Reason_euthanasiaSerializer(reason_euthanasia)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_reason_euthanasia(request, pk):
    try:
        reason_euthanasia = Reason_euthanasia.objects.get(pk=pk)
        reason_euthanasia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# District
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_district(request):
    try:
        district = District.objects.filter(**request.query_params)
        serializer = DistrictSerializer(district, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_district(request):
    try:
        district = District.objects.create(**request.query_params)
        serializer = DistrictSerializer(district)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_district(request, pk):
    try:
        district = District.objects.filter(pk=pk)
        district.update(**request.query_params)
        district = District.objects.get(pk=pk)
        serializer = DistrictSerializer(district)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_district(request, pk):
    try:
        district = District.objects.get(pk=pk)
        district.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Size
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_size(request):
    try:
        size = Size.objects.filter(**request.query_params)
        serializer = SizeSerializer(size, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_size(request):
    try:
        size = Size.objects.create(**request.query_params)
        serializer = SizeSerializer(size)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_size(request, pk):
    try:
        size = Size.objects.filter(pk=pk)
        size.update(**request.query_params)
        size = Size.objects.get(pk=pk)
        serializer = SizeSerializer(size)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_size(request, pk):
    try:
        size = Size.objects.get(pk=pk)
        size.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Tail
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_tail(request):
    try:
        tail = Tail.objects.filter(**request.query_params)
        serializer = TailSerializer(tail, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_tail(request):
    try:
        tail = Tail.objects.create(**request.query_params)
        serializer = TailSerializer(tail)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_tail(request, pk):
    try:
        tail = Tail.objects.filter(pk=pk)
        tail.update(**request.query_params)
        tail = Tail.objects.get(pk=pk)
        serializer = TailSerializer(tail)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_tail(request, pk):
    try:
        tail = Tail.objects.get(pk=pk)
        tail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Ears
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_ears(request):
    try:
        ears = Ears.objects.filter(**request.query_params)
        serializer = EarsSerializer(ears, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_ears(request):
    try:
        ears = Ears.objects.create(**request.query_params)
        serializer = EarsSerializer(ears)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_ears(request, pk):
    try:
        ears = Ears.objects.filter(pk=pk)
        ears.update(**request.query_params)
        ears = Ears.objects.get(pk=pk)
        serializer = EarsSerializer(ears)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_ears(request, pk):
    try:
        ears = Ears.objects.get(pk=pk)
        ears.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Wool
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_wool(request):
    try:
        wool = Wool.objects.filter(**request.query_params)
        serializer = WoolSerializer(wool, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_wool(request):
    try:
        wool = Wool.objects.create(**request.query_params)
        serializer = WoolSerializer(wool)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_wool(request, pk):
    try:
        wool = Wool.objects.filter(pk=pk)
        wool.update(**request.query_params)
        wool = Wool.objects.get(pk=pk)
        serializer = WoolSerializer(wool)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_wool(request, pk):
    try:
        wool = Wool.objects.get(pk=pk)
        wool.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Color
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_color(request):
    try:
        color = Color.objects.filter(**request.query_params)
        serializer = ColorSerializer(color, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_color(request):
    try:
        color = Color.objects.create(**request.query_params)
        serializer = ColorSerializer(color)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_color(request, pk):
    try:
        color = Color.objects.filter(pk=pk)
        color.update(**request.query_params)
        color = Color.objects.get(pk=pk)
        serializer = ColorSerializer(color)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_color(request, pk):
    try:
        color = Color.objects.get(pk=pk)
        color.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Breed
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_breed(request):
    try:
        breed = Breed.objects.filter(**request.query_params)
        serializer = BreedSerializer(breed, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_breed(request):
    try:
        breed = Breed.objects.create(**request.query_params)
        serializer = BreedSerializer(breed)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_breed(request, pk):
    try:
        breed = Breed.objects.filter(pk=pk)
        breed.update(**request.query_params)
        breed = Breed.objects.get(pk=pk)
        serializer = BreedSerializer(breed)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_breed(request, pk):
    try:
        breed = Breed.objects.get(pk=pk)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Sex
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_sex(request):
    try:
        sex = Sex.objects.filter(**request.query_params)
        serializer = SexSerializer(sex, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_sex(request):
    try:
        sex = Sex.objects.create(**request.query_params)
        serializer = SexSerializer(sex)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_sex(request, pk):
    try:
        sex = Sex.objects.filter(pk=pk)
        sex.update(**request.query_params)
        sex = Sex.objects.get(pk=pk)
        serializer = SexSerializer(sex)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_sex(request, pk):
    try:
        sex = Sex.objects.get(pk=pk)
        sex.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Kind
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_kind(request):
    try:
        kind = Kind.objects.filter(**request.query_params)
        serializer = KindSerializer(kind, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_kind(request):
    try:
        kind = Kind.objects.create(**request.query_params)
        serializer = KindSerializer(kind)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_kind(request, pk):
    try:
        kind = Kind.objects.filter(pk=pk)
        kind.update(**request.query_params)
        kind = Kind.objects.get(pk=pk)
        serializer = KindSerializer(kind)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_kind(request, pk):
    try:
        kind = Kind.objects.get(pk=pk)
        kind.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Pet
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_pet(request):
    try:
        pet = Pet.objects.filter(**request.query_params)
        serializer = PetSerializer(pet, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_pet(request):
    try:
        pet = Pet()
        pet.ids = request.query_params['ids']
        pet.kind = Kind.objects.get(pk=int(request.query_params['kind']))
        pet.age = request.query_params['age']
        pet.weight = request.query_params['weight']
        pet.name = request.query_params['name']
        pet.sex = Sex.objects.get(pk=int(request.query_params['sex']))
        pet.breed = Breed.objects.get(pk=int(request.query_params['breed']))
        pet.color = Color.objects.get(pk=int(request.query_params['color']))
        pet.wool = Wool.objects.get(pk=int(request.query_params['wool']))
        pet.ears = Ears.objects.get(pk=int(request.query_params['ears']))
        pet.tail = Tail.objects.get(pk=int(request.query_params['tail']))
        pet.size = Size.objects.get(pk=int(request.query_params['size']))
        pet.special_signs = request.query_params['special_signs']
        if 'aviary' in request.query_params:
            pet.aviary = request.query_params['aviary']
        if 'identification_mark' in request.query_params:
            pet.identification_mark = request.query_params['identification_mark']
        if 'sterilization_date' in request.query_params:
            pet.sterilization_date = request.query_params['sterilization_date']
        if 'name_veterinarian' in request.query_params:
            pet.name_veterinarian = request.query_params['name_veterinarian']
        pet.socialized = request.query_params['socialized']
        if 'work_order' in request.query_params:
            pet.work_order = request.query_params['work_order']
        if 'work_order_date' in request.query_params:
            pet.work_order_date = request.query_params['work_order_date']
        if 'district' in request.query_params:
            pet.district = District.objects.get(pk=int(request.query_params['district']))
        if 'catch_report' in request.query_params:
            pet.catch_report = request.query_params['catch_report']
        if 'catching_address' in request.query_params:
            pet.catching_address = request.query_params['catching_address']
        if 'entity' in request.query_params:
            pet.entity = request.query_params['entity']
        if 'name_guardians' in request.query_params:
            pet.name_guardians = request.query_params['name_guardians']
        if 'natural_person_name' in request.query_params:
            pet.natural_person_name = request.query_params['natural_person_name']
        if 'date_to_shelter' in request.query_params:
            pet.date_to_shelter = request.query_params['date_to_shelter']
        if 'act_no' in request.query_params:
            pet.act_no = request.query_params['act_no']
        if 'date_leaving_shelter' in request.query_params:
            pet.date_leaving_shelter = request.query_params['date_leaving_shelter']
        if 'reason_retirement' in request.query_params:
            pet.reason_retirement = Reason_retirement.objects.get(pk=int(request.query_params['reason_retirement']))
        if 'reason_death' in request.query_params:
            pet.reason_death = Reason_death.objects.get(pk=int(request.query_params['reason_death']))
        if 'reason_euthanasia' in request.query_params:
            pet.reason_euthanasia = Reason_euthanasia.objects.get(pk=int(request.query_params['reason_euthanasia']))
        if 'act_retirement' in request.query_params:
            pet.act_retirement = request.query_params['act_retirement']
        pet.shelter = Shelter.objects.get(pk=int(request.query_params['shelter']))
        pet.operating_organizations = Operating_organizations.objects.get(pk=int(request.query_params['operating_organizations']))
        pet.name_leader_shelter = request.query_params['name_leader_shelter']
        pet.name_care_worker = request.query_params['name_care_worker']
        pet.save()
        serializer = PetSerializer(pet)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_pet(request, pk):
    try:
        pet = Pet.objects.filter(pk=pk)
        if 'ids' in request.query_params:
            pet.ids = request.query_params['ids']
        if 'kind' in request.query_params:
            pet.kind = Kind.objects.get(pk=int(request.query_params['kind']))
        if 'age' in request.query_params:
            pet.age = request.query_params['age']
        if 'weight' in request.query_params:
            pet.weight = request.query_params['weight']
        if 'name' in request.query_params:
            pet.name = request.query_params['name']
        if 'sex' in request.query_params:
            pet.sex = Sex.objects.get(pk=int(request.query_params['sex']))
        if 'breed' in request.query_params:
            pet.breed = Breed.objects.get(pk=int(request.query_params['breed']))
        if 'color' in request.query_params:
            pet.color = Color.objects.get(pk=int(request.query_params['color']))
        if 'wool' in request.query_params:
            pet.wool = Wool.objects.get(pk=int(request.query_params['wool']))
        if 'ears' in request.query_params:
            pet.ears = Ears.objects.get(pk=int(request.query_params['ears']))
        if 'tail' in request.query_params:
            pet.tail = Tail.objects.get(pk=int(request.query_params['tail']))
        if 'size' in request.query_params:
            pet.size = Size.objects.get(pk=int(request.query_params['size']))
        if 'special_signs' in request.query_params:
            pet.special_signs = request.query_params['special_signs']
        if 'aviary' in request.query_params:
            pet.aviary = request.query_params['aviary']
        if 'identification_mark' in request.query_params:
            pet.identification_mark = request.query_params['identification_mark']
        if 'sterilization_date' in request.query_params:
            pet.sterilization_date = request.query_params['sterilization_date']
        if 'name_veterinarian' in request.query_params:
            pet.name_veterinarian = request.query_params['name_veterinarian']
        if 'socialized' in request.query_params:
            pet.socialized = request.query_params['socialized']
        if 'work_order' in request.query_params:
            pet.work_order = request.query_params['work_order']
        if 'work_order_date' in request.query_params:
            pet.work_order_date = request.query_params['work_order_date']
        if 'district' in request.query_params:
            pet.district = District.objects.get(pk=int(request.query_params['district']))
        if 'catch_report' in request.query_params:
            pet.catch_report = request.query_params['catch_report']
        if 'catching_address' in request.query_params:
            pet.catching_address = request.query_params['catching_address']
        if 'entity' in request.query_params:
            pet.entity = request.query_params['entity']
        if 'name_guardians' in request.query_params:
            pet.name_guardians = request.query_params['name_guardians']
        if 'natural_person_name' in request.query_params:
            pet.natural_person_name = request.query_params['natural_person_name']
        if 'date_to_shelter' in request.query_params:
            pet.date_to_shelter = request.query_params['date_to_shelter']
        if 'act_no' in request.query_params:
            pet.act_no = request.query_params['act_no']
        if 'date_leaving_shelter' in request.query_params:
            pet.date_leaving_shelter = request.query_params['date_leaving_shelter']
        if 'reason_retirement' in request.query_params:
            pet.reason_retirement = Reason_retirement.objects.get(pk=int(request.query_params['reason_retirement']))
        if 'reason_death' in request.query_params:
            pet.reason_death = Reason_death.objects.get(pk=int(request.query_params['reason_death']))
        if 'reason_euthanasia' in request.query_params:
            pet.reason_euthanasia = Reason_euthanasia.objects.get(pk=int(request.query_params['reason_euthanasia']))
        if 'act_retirement' in request.query_params:
            pet.act_retirement = request.query_params['act_retirement']
        if 'shelter' in request.query_params:
            pet.shelter = Shelter.objects.get(pk=int(request.query_params['shelter']))
        if 'operating_organizations' in request.query_params:
            pet.operating_organizations = Operating_organizations.objects.get(pk=int(request.query_params['operating_organizations']))
        if 'name_leader_shelter' in request.query_params:
            pet.name_leader_shelter = request.query_params['name_leader_shelter']
        if 'name_care_worker' in request.query_params:
            pet.name_care_worker = request.query_params['name_care_worker']
        pet.save()
        pet = Pet.objects.get(pk=pk)
        serializer = PetSerializer(pet)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_pet(request, pk):
    try:
        pet = Pet.objects.get(pk=pk)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Processing_parasites
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_processing_parasites(request):
    try:
        processing_parasites = Processing_parasites.objects.filter(**request.query_params)
        serializer = Processing_parasitesSerializer(processing_parasites, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_processing_parasites(request):
    try:
        processing_parasites = Processing_parasites()
        processing_parasites.no = request.query_params['no']
        processing_parasites.date = request.query_params['date']
        processing_parasites.drug_name = request.query_params['drug_name']
        processing_parasites.dose = request.query_params['dose']
        processing_parasites.pet = Pet.objects.get(pk=int(request.query_params['pet']))
        processing_parasites.save()
        serializer = Processing_parasitesSerializer(processing_parasites)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_processing_parasites(request, pk):
    try:
        processing_parasites = Processing_parasites.objects.filter(pk=pk)
        if 'no' in request.query_params:
            processing_parasites.no = request.query_params['no']
        if 'date' in request.query_params:
            processing_parasites.date = request.query_params['date']
        if 'drug_name' in request.query_params:
            processing_parasites.drug_name = request.query_params['drug_name']
        if 'dose' in request.query_params:
            processing_parasites.dose = request.query_params['dose']
        if 'pet' in request.query_params:
            processing_parasites.pet = Pet.objects.get(pk=int(request.query_params['pet']))
        processing_parasites.save()
        processing_parasites = Processing_parasites.objects.get(pk=pk)
        serializer = Processing_parasitesSerializer(processing_parasites)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_processing_parasites(request, pk):
    try:
        processing_parasites = Processing_parasites.objects.get(pk=pk)
        processing_parasites.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Vaccination_information
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_vaccination_information(request):
    try:
        vaccination_information = Vaccination_information.objects.filter(**request.query_params)
        serializer = Vaccination_informationSerializer(vaccination_information, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_vaccination_information(request):
    try:
        vaccination_information = Vaccination_information()
        vaccination_information.no = request.query_params['no']
        vaccination_information.date = request.query_params['date']
        vaccination_information.type_vaccine = request.query_params['type_vaccine']
        vaccination_information.series = request.query_params['series']
        vaccination_information.pet = Pet.objects.get(pk=int(request.query_params['pet']))
        vaccination_information.save()
        serializer = Vaccination_informationSerializer(vaccination_information)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_vaccination_information(request, pk):
    try:
        vaccination_information = Vaccination_information.objects.filter(pk=pk)
        if 'no' in request.query_params:
            vaccination_information.no = request.query_params['no']
        if 'date' in request.query_params:
            vaccination_information.date = request.query_params['date']
        if 'type_vaccine' in request.query_params:
            vaccination_information.type_vaccine = request.query_params['type_vaccine']
        if 'series' in request.query_params:
            vaccination_information.series = request.query_params['series']
        if 'pet' in request.query_params:
            vaccination_information.pet = Pet.objects.get(pk=int(request.query_params['pet']))
        vaccination_information.save()
        vaccination_information = Vaccination_information.objects.get(pk=pk)
        serializer = Vaccination_informationSerializer(vaccination_information)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_vaccination_information(request, pk):
    try:
        vaccination_information = Vaccination_information.objects.get(pk=pk)
        vaccination_information.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Health_information
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_health_information(request):
    try:
        health_information = Health_information.objects.filter(**request.query_params)
        serializer = Health_informationSerializer(health_information, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_health_information(request):
    try:
        health_information = Health_information()
        health_information.date = request.query_params['date']
        health_information.anamnesis = request.query_params['anamnesis']
        health_information.pet = Pet.objects.get(pk=int(request.query_params['pet']))
        health_information.save()
        serializer = Health_informationSerializer(health_information)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_health_information(request, pk):
    try:
        health_information = Health_information.objects.filter(pk=pk)
        if 'date' in request.query_params:
            health_information.date = request.query_params['date']
        if 'anamnesis' in request.query_params:
            health_information.anamnesis = request.query_params['anamnesis']
        if 'pet' in request.query_params:
            health_information.pet = Pet.objects.get(pk=int(request.query_params['pet']))
        health_information.save()
        health_information = Health_information.objects.get(pk=pk)
        serializer = Health_informationSerializer(health_information)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_health_information(request, pk):
    try:
        health_information = Health_information.objects.get(pk=pk)
        health_information.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


