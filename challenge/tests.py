from django.test import TestCase, Client

from challenge.compute import _compute_zone_carbon_impact, _compute_exploitation_zone_carbon_impact
from challenge.data import get_zone, get_building


# Create your tests here.
class Level1Test(TestCase):
    def test_query_error(self):
        c = Client()
        response = c.get("/total_surface")
        self.assertEqual(response.status_code, 400)
        response = c.get("/total_surface?building_id=a")
        self.assertEqual(response.status_code, 400)
        response = c.get("/building_usage")
        self.assertEqual(response.status_code, 400)
        response = c.get("/building_usage?building_id=b")
        self.assertEqual(response.status_code, 400)

    def test_query_not_found(self):
        c = Client()
        response = c.get("/total_surface?building_id=6")
        self.assertEqual(response.status_code, 404)
        response = c.get("/building_usage?building_id=6")
        self.assertEqual(response.status_code, 404)

    def test_get_surface(self):
        c = Client()
        response = c.get("/total_surface?building_id=0")
        self.assertIsNotNone(response.json())
        self.assertIs(type(response.json()), int)
        self.assertEqual(response.status_code, 200)

    def test_get_usage(self):
        c = Client()
        response = c.get("/building_usage?building_id=0")
        self.assertIsNotNone(response.json())
        self.assertIs(type(response.json()), str)
        self.assertEqual(response.status_code, 200)


class Level2Test(TestCase):
    def test_query_error(self):
        c = Client()
        response = c.get("/carbon_impact")
        self.assertEqual(response.status_code, 400)
        response = c.get("/total_surface?building_id=a")
        self.assertEqual(response.status_code, 400)
        response = c.get("/total_surface?building_id=6")
        self.assertEqual(response.status_code, 404)

    def test_carbon_impact_computation(self):
        building = get_building(0)
        zone = get_zone(0)
        result = _compute_zone_carbon_impact(zone, 'production')
        self.assertIs(type(result), float)
        result = _compute_zone_carbon_impact(zone, 'construction')
        self.assertIs(type(result), float)
        result = _compute_zone_carbon_impact(zone, 'finDeVie')
        self.assertIs(type(result), float)
        result = _compute_exploitation_zone_carbon_impact(zone, building['periodeDeReference'])
        self.assertIs(type(result), float)

    def test_query_carbon_impact(self):
        c = Client()
        response = c.get("/total_surface?building_id=2")
        self.assertEqual(response.status_code, 200)
        self.assertGreater(response.json(), 0)
