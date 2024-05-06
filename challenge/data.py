import json


def get_buildings():
    json_buildings = open('./data/batiments.json').read()
    return json.loads(json_buildings)


def get_building(building_id):
    buildings = get_buildings()
    result = [x for x in buildings if x['id'] == int(building_id)]
    return result[0] if result else None


def get_zones():
    json_zones = open('./data/zones.json').read()
    return json.loads(json_zones)


def get_usages():
    json_zones = open('./data/usages.json').read()
    return json.loads(json_zones)
