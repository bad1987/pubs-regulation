import asyncio
from unittest import TestCase
import unittest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
import sys
sys.path.append("../..")

from schemas.QuartierAffichageSchema import QuartierAffichageSchema

from models.quartierAffichage import QuartierAffichage
from models.zoneAffichage import ZoneAffichage

from main import app
from db.Connexion import SessionLocal

class TestQuartierAffichage(TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.db = SessionLocal()
        # Create test data for zoneAffichage
        self.zone_1 = ZoneAffichage(CodeZone="ABC", LibelleZone="Test Zone")
        self.db.add(self.zone_1)
        # Create test data for quartierAffichage
        self.quartier_affich = QuartierAffichage(NomQuartier="Test Quartier", SousQuartierAffich="Test Sous Quartier", ObservationsQuartier="Test Observations", ArrondissementQaurtier="Test Arrondissement", IDZoneAffichage=self.zone_1.IDZoneAffichage)
        self.quartier_affich.zone_affichage = self.zone_1
        self.db.add(self.quartier_affich)
        self.db.commit()
        self.db.refresh(self.quartier_affich)
        self.db.refresh(self.zone_1)
 
    def tearDown(self):
        # Remove test data
        QuartierAffichage.delete(self.db, self.quartier_affich.IDQuartierAffichage)
        ZoneAffichage.delete(self.db, self.zone_1.IDZoneAffichage)
        self.db.commit()
        self.db.close()
 
    def test_get_quartier_affichage_by_id(self):
        # Test case 1: Valid quartier_affichage_id
        quartier_affichage_id = self.quartier_affich.IDQuartierAffichage
        expected_result = QuartierAffichageSchema(**jsonable_encoder(self.quartier_affich))
        response = self.client.get(f'/quartierAffichages/{quartier_affichage_id}')
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result.dict())

        # Test case 2: Invalid quartier_affichage_id
        quartier_affichage_id = 1
        expected_error = {'detail': 'QuartierAffichage not found'}
        response = self.client.get(f'/quartierAffichages/{quartier_affichage_id}')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), expected_error)
    
    # test the post route
    def test_create_quartier_affichage(self):
        # create test data
        post_data = {
            "NomQuartier": "Create Test Quartier",
            "SousQuartierAffich": "Create Test Sous Quartier",
            "ObservationsQuartier": "Create Test Observations",
            "ArrondissementQaurtier": "Create Test Arrondissement",
            "IDZoneAffichage": self.zone_1.IDZoneAffichage
        }
        response = self.client.post("/quartierAffichages", json=post_data)
        self.assertEqual(response.status_code, 201)
        expected_result = self.client.get(f'/quartierAffichages/nomQuartier', params={"NomQuartier": post_data["NomQuartier"]})
        print(expected_result.json())
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())

        # clean up using delete endpoint
        response = self.client.delete(f'/quartierAffichages/{response.json()["IDQuartierAffichage"]}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()