from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema, OpenApiParameter

from challenge.compute import get_total_building_area, get_building_usage, compute_building_carbon_impact


@extend_schema(
    parameters=[OpenApiParameter(name='building_id',
                                 description='Building id for which compute surface', required=True, type=int)],
    description='Compute and return the surface of the specified building',
    auth=None,
    responses={200: int},
)
@api_view(['GET'])
def total_surface(request: Request) -> Response:
    building_id = request.query_params.get('building_id')
    if not building_id or not building_id.isnumeric():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    result = get_total_building_area(building_id)
    return Response(result)


@extend_schema(
    parameters=[OpenApiParameter(name='building_id',
                                 description='Building id for which retrieve usage label', required=True, type=int)],
    description='Retrieve the usage label of the specified building',
    auth=None,
    responses={200: str},
)
@api_view(['GET'])
def building_usage(request: Request) -> Response:
    building_id = request.query_params.get('building_id')
    if not building_id or not building_id.isnumeric():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    result = get_building_usage(building_id)
    return Response(result)


@extend_schema(
    parameters=[OpenApiParameter(name='building_id',
                                 description='Building id for which compute carbon impact', required=True, type=int)],
    description='Compute and return the total carbon impact of the specified building',
    auth=None,
    responses={200: float},
)
@api_view(['GET'])
def carbon_impact(request: Request) -> Response:
    building_id = request.query_params.get('building_id')
    if not building_id or not building_id.isnumeric():
        return Response(status=status.HTTP_400_BAD_REQUEST)
    result = compute_building_carbon_impact(building_id)
    return Response(result)
