from django.http import Http404

from challenge.data import get_building, get_zones, get_usages


def get_total_building_area(building_id: int):
    building = get_building(building_id)
    if not building:
        raise Http404
    zones = get_zones()
    total_surface = 0
    for zone_id in building['zoneIds']:
        zone = [x for x in zones if x['id'] == int(zone_id)]
        if zone:
            total_surface += zone[0]['surface']
    return total_surface


def get_building_usage(building_id: int):
    building = get_building(building_id)
    if not building:
        raise Http404
    usages = get_usages()
    zones = get_zones()
    max_surface = 0
    usage_label = None
    for zone_id in building['zoneIds']:
        zone = [x for x in zones if x['id'] == int(zone_id)]
        if zone and zone[0]['surface'] > max_surface:
            max_surface = zone[0]['surface']
            usage_label = usages[str(zone[0]['usage'])]
    return usage_label

