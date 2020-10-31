import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
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

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_prefecture(request):
    try:
        prefecture = Prefecture.objects.create(**request.query_params)
        serializer = PrefectureSerializer(prefecture, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_prefecture(request, id_):
    try:
        prefecture = Prefecture.objects.get(pk=id_)
        prefecture.update(**request.query_params)
        serializer = PrefectureSerializer(prefecture, many=True)
        return JsonResponse({'ok': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def delete_prefecture(request, id_):
    try:
        prefecture = Prefecture.objects.get(pk=id_)
        prefecture.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


