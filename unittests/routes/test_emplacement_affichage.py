import asyncio
import datetime
from unittest import TestCase
import unittest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
import sys
sys.path.append("../..")

from models.emplacementAffichage import EmplacementAffichage
from models.quartierAffichage import QuartierAffichage
from models.zoneAffichage import ZoneAffichage
from schemas.EmplacementAffichageSchema import EmplacementAffichageSchema

from main import app
from db.Connexion import SessionLocal

class TestEmplacementAffichage(TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.db = SessionLocal()
        # create zoneAffichage test data
        self.zone_affichage = ZoneAffichage(CodeZone="ABC", LibelleZone="Test Zone")
        self.db.add(self.zone_affichage)
        # create quartierAffichage test data
        self.quartier_affich = QuartierAffichage(NomQuartier="Test Quartier", SousQuartierAffich="Test Sous Quartier", ObservationsQuartier="Test Observations", ArrondissementQuartier="Test Arrondissement", IDZoneAffichage=self.zone_affichage.IDZoneAffichage)
        self.quartier_affich.zone_affichage = self.zone_affichage
        self.db.add(self.quartier_affich)
        # create emplacementAffichage test data
        self.emplacement_affichage = EmplacementAffichage(CodeEmplacement="XYZ", IDQuartierAffichage=self.quartier_affich.IDQuartierAffichage)
        self.emplacement_affichage.quartier = self.quartier_affich
        self.db.add(self.emplacement_affichage)
        self.db.commit()
        self.db.refresh(self.zone_affichage)
        self.db.refresh(self.quartier_affich)
        self.db.refresh(self.emplacement_affichage)

    def tearDown(self):
        ZoneAffichage.delete(self.db, self.zone_affichage.IDZoneAffichage)
        QuartierAffichage.delete(self.db, self.quartier_affich.IDQuartierAffichage)
        EmplacementAffichage.delete(self.db, self.emplacement_affichage.IDEmplacementAffichage)
        self.db.close()
    
    def test_get_emplacement_affichage_by_id(self):
        # Test case 1: Valid emplacement_affichage_id
        emplacement_affichage_id = self.emplacement_affichage.IDEmplacementAffichage
        response = self.client.get(f'/emplacementAffichage/{emplacement_affichage_id}')
        print(response.json())
        self.assertEqual(response.status_code, 200)
        expected_result = EmplacementAffichageSchema.from_orm(self.emplacement_affichage)
        self.assertEqual(response.json(), expected_result.dict())

        # Test case 2: Invalid emplacement_affichage_id
        emplacement_affichage_id = 10000
        expected_error = {'detail': 'EmplacementAffichage not found'}
        response = self.client.get(f'/emplacementAffichage/{emplacement_affichage_id}')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), expected_error)
    
    def test_get_emplacement_affichage_by_code(self):
        # Test case 1: Valid emplacement_affichage_code
        emplacement_affichage_code = self.emplacement_affichage.CodeEmplacement
        response = self.client.get(f'/emplacementAffichage/code', params={'CodeEmplacement': emplacement_affichage_code})
        print(response.json())
        self.assertEqual(response.status_code, 200)
        expected_result = EmplacementAffichageSchema.from_orm(self.emplacement_affichage)
        self.assertEqual(response.json(), expected_result.dict())

        # Test case 2: Invalid emplacement_affichage_code
        emplacement_affichage_code = "AYZ"
        expected_error = {'detail': 'EmplacementAffichage not found'}
        response = self.client.get(f'/emplacementAffichage/code', params={'CodeEmplacement': emplacement_affichage_code})
        self.assertEqual(response.status_code, 404)

    def test_get_emplacement_quartier_affichage_by_id(self):
        # Test case 1: Valid emplacement_affichage_id
        quartier_affichage_id = self.emplacement_affichage.IDQuartierAffichage
        response = self.client.get(f'/emplacementAffichage/quartier', params={'IDQuartierAffichage': quartier_affichage_id})
        self.assertEqual(response.status_code, 200)
        expected_result = EmplacementAffichageSchema.from_orm(self.emplacement_affichage)
        self.assertEqual(response.json(), [expected_result.dict()])

        # Test case 2: Invalid quartier_affichage_id
        quartier_affichage_id = 10000
        expected_response = []
        response = self.client.get(f'/emplacementAffichage/quartier', params={'IDQuartierAffichage': quartier_affichage_id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)
    
    def test_get_all(self):
        response = self.client.get('/emplacementAffichage')
        self.assertEqual(response.status_code, 200)
        expected_result = EmplacementAffichageSchema.from_orm(self.emplacement_affichage)
        self.assertEqual(response.json(), [expected_result.dict()])
    
    def test_create_emplacement_affichage(self):
        post_data = {
            "CodeEmplacement": "ZYX",
            "IDQuartierAffichage": self.quartier_affich.IDQuartierAffichage
        }
        response = self.client.post('/emplacementAffichage', json=post_data)
        self.assertEqual(response.status_code, 201)
        expected_result = self.client.get('/emplacementAffichage/code', params={'CodeEmplacement': post_data['CodeEmplacement']})
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())

        # clean up using delete endpoint
        response = self.client.delete(f'/emplacementAffichage/{response.json()["IDEmplacementAffichage"]}')
        self.assertEqual(response.status_code, 204)

    def test_update_emplacement_affichage(self):
        post_data = {
            "IDEmplacementAffichage": self.emplacement_affichage.IDEmplacementAffichage,
            "CodeEmplacement": "ABC",
            "IDQuartierAffichage": self.quartier_affich.IDQuartierAffichage
        }
        response = self.client.put(f'/emplacementAffichage/{self.emplacement_affichage.IDEmplacementAffichage}', json=post_data)
        self.assertEqual(response.status_code, 200)
        expected_result = self.client.get(f'/emplacementAffichage/{self.emplacement_affichage.IDEmplacementAffichage}')
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())

if __name__ == '__main__':
    unittest.main()