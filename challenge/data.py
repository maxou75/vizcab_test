import json


def get_buildings() -> list:
    json_buildings = open('./challenge/data/batiments.json').read()
    return json.loads(json_buildings)


def get_building(building_id: int) -> dict | None:
    buildings = get_buildings()
    result = [x for x in buildings if x['id'] == int(building_id)]
    return result[0] if result else None


def get_zones() -> list:
    json_zones = open('./challenge/data/zones.json').read()
    return json.loads(json_zones)


def get_zone(zone_id: int) -> dict | None:
    buildings = get_zones()
    result = [x for x in buildings if x['id'] == int(zone_id)]
    return result[0] if result else None


def get_usages() -> list:
    json_zones = open('./challenge/data/usages.json').read()
    return json.loads(json_zones)


def get_construction_elements() -> list:
    json_buildings = open('./challenge/data/construction_elements.json').read()
    return json.loads(json_buildings)


def get_construction_element(construction_element_id: int) -> dict | None:
    construction_elements = get_construction_elements()
    result = [x for x in construction_elements if x['id'] == int(construction_element_id)]
    return result[0] if result else None
