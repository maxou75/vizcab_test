from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from challenge.compute import get_total_building_area, get_building_usage


@api_view(['GET'])
def total_surface_calculation(request):
    building_id = request.query_params.get('building_id')
    if not building_id or not building_id.isnumeric():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    result = get_total_building_area(building_id)
    return Response(result)


@api_view(['GET'])
def building_usage(request):
    building_id = request.query_params.get('building_id')
    if not building_id.isnumeric():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    result = get_building_usage(building_id)
    return Response(result)
