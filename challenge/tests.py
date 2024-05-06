from django.test import TestCase, Client


# Create your tests here.
class Level1Test(TestCase):
    def test_query_error(self):
        c = Client()
        response = c.get("/total_surface_calculation")
        self.assertEqual(response.status_code, 400)
        response = c.get("/total_surface_calculation?building_id=a")
        self.assertEqual(response.status_code, 400)

    def test_query_not_found(self):
        c = Client()
        response = c.get("/total_surface_calculation?building_id=6")
        self.assertEqual(response.status_code, 404)

    def test_get_surface(self):
        c = Client()
        response = c.get("/total_surface_calculation?building_id=0")
        self.assertIsNotNone(response.json())
        self.assertEqual(response.status_code, 200)

    def test_get_usage(self):
        c = Client()
        response = c.get("/building_usage?building_id=0")
        self.assertEqual(response.json(), "Logement collectif")
        self.assertEqual(response.status_code, 200)


