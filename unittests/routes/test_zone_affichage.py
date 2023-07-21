import asyncio
from unittest import TestCase
import unittest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
import sys
sys.path.append("../..")

from schemas.ZoneAffichage import ZoneAffichageSchema

from models.zoneAffichage import ZoneAffichage

from main import app
from db.Connexion import SessionLocal

class TestZoneAffichage(TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.db = SessionLocal()
        # create test data
        self.zone_affichage = ZoneAffichage(CodeZone="ABC", LibelleZone="Test Zone")
        self.db.add(self.zone_affichage)
        self.db.commit()
        self.db.refresh(self.zone_affichage)

    def tearDown(self):
        # Remove test data
        ZoneAffichage.delete(self.db, self.zone_affichage.IDZoneAffichage)
        self.db.commit()
        self.db.close()

    def test_get(self):
        # test case 1 : valid zone_affichage_id
        response = self.client.get(f"/zoneAffichages/{self.zone_affichage.IDZoneAffichage}")
        self.assertEqual(response.status_code, 200)
        expected_result = ZoneAffichageSchema(**jsonable_encoder(self.zone_affichage)).dict()
        self.assertEqual(response.json(), expected_result)

        # test case 2 : invalid zone_affichage_id
        response = self.client.get(f"/zoneAffichages/1000000")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'ZoneAffichage not found'})
    
    def test_get_by_codeZone(self):
        # test case 1 : valid zone_affichage_code
        response = self.client.get(f"/zoneAffichages/codeZone", params={'codeZone': self.zone_affichage.CodeZone})
        self.assertEqual(response.status_code, 200)
        expected_result = ZoneAffichageSchema(**jsonable_encoder(self.zone_affichage)).dict()
        self.assertEqual(response.json(), expected_result)

        # test case 2 : invalid zone_affichage_code
        response = self.client.get(f"/zoneAffichages/codeZone", params={'codeZone': "DEF"})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'ZoneAffichage not found'})

    def test_get_all(self):
        expected_result = [ZoneAffichageSchema(**jsonable_encoder(self.zone_affichage)).dict()]
        response = self.client.get("/zoneAffichages")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result)

    def test_create(self):
        post_data = {
            "CodeZone": "XYZ",
            "LibelleZone": "Test Zone"
        }
        response = self.client.post("/zoneAffichages", json=post_data)
        self.assertEqual(response.status_code, 201)
        expected_result = self.client.get("/zoneAffichages/codeZone", params={'codeZone': post_data['CodeZone']})
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())

        # clean up using delete endpoint
        response = self.client.delete(f"/zoneAffichages/{response.json()['IDZoneAffichage']}")
        self.assertEqual(response.status_code, 204)

    def test_update(self):
        post_data = {
            "IDZoneAffichage": self.zone_affichage.IDZoneAffichage,
            "CodeZone": "UYZ",
            "LibelleZone": "Update Zone"
        }
        response = self.client.put(f"/zoneAffichages/{self.zone_affichage.IDZoneAffichage}", json=post_data)
        self.assertEqual(response.status_code, 200)
        expected_result = self.client.get("/zoneAffichages/codeZone", params={'codeZone': post_data['CodeZone']})
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())

if __name__ == '__main__':
    unittest.main()