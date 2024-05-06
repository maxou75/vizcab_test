from django.http import Http404

from challenge.data import get_building, get_zones, get_usages, get_zone, get_construction_element


def get_total_building_area(building_id: int) -> int:
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


def get_building_usage(building_id: int) -> str:
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


def _compute_zone_carbon_impact(zone: dict, cycle: str) -> float:
    result = 0
    for construction_element in zone['constructionElements']:
        construction_element_item = get_construction_element(construction_element['id'])
        impacts = construction_element_item['impactUnitaireRechauffementClimatique'] \
            if construction_element_item else None
        result += float(impacts[cycle]) * float(construction_element['quantite'])
    return result


def _compute_exploitation_zone_carbon_impact(zone: dict, period_reference: int) -> float:
    result = 0
    for construction_element in zone['constructionElements']:
        construction_element_item = get_construction_element(construction_element['id'])
        coefficient = max(1, period_reference / construction_element_item['dureeVieTypique'])
        impacts = construction_element_item['impactUnitaireRechauffementClimatique'] \
            if construction_element_item else None
        result += ((coefficient * impacts['exploitation'] +
                    (coefficient - 1) * (impacts['production'] + impacts['construction'] + impacts['finDeVie']))
                   * construction_element['quantite'])
    return result


def compute_building_carbon_impact(building_id: int) -> float:
    building = get_building(building_id)
    if not building:
        raise Http404
    production_impact = 0
    construction_impact = 0
    exploitation_impact = 0
    end_impact = 0
    for zone_id in building['zoneIds']:
        zone = get_zone(zone_id)
        production_impact += _compute_zone_carbon_impact(zone, 'production')
        construction_impact += _compute_zone_carbon_impact(zone, 'construction')
        exploitation_impact = _compute_exploitation_zone_carbon_impact(zone, building['periodeDeReference'])
        end_impact += _compute_zone_carbon_impact(zone, 'finDeVie')
    return production_impact + construction_impact + exploitation_impact + end_impact
