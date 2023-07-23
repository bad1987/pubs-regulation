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
        self.quartier_affich = QuartierAffichage(NomQuartier="Test Quartier", SousQuartierAffich="Test Sous Quartier", ObservationsQuartier="Test Observations", ArrondissementQuartier="Test Arrondissement", IDZoneAffichage=self.zone_1.IDZoneAffichage)
        self.quartier_affich.zone_affichage = self.zone_affichage
        self.db.add(self.quartier_affich)
        # create emplacementAffichage test data
        self.emplacement_affichage = EmplacementAffichage(CodeEmplacement="ABC", IDQuartierAffichage=self.quartier_affich.IDQuartierAffichage)
        self.db.add(self.emplacement_affichage)
        self.db.commit()
        self.db.refresh(self.emplacement_affichage)
        self.db.refresh(self.quartier_affich)
        self.db.refresh(self.zone_affichage)

    def tearDown(self):
        ZoneAffichage.delete(self.db, self.zone_affichage)
        self.db.commit()
        self.db.close()
    
    def test_get_emplacement_affichage_by_id(self):
        # Test case 1: Valid emplacement_affichage_id
        emplacement_affichage_id = self.emplacement_affichage.IDEmplacementAffichage
        expected_result = EmplacementAffichageSchema(**jsonable_encoder(self.emplacement_affichage))
        response = self.client.get(f'/emplacementAffichages/{emplacement_affichage_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result.dict())

        # Test case 2: Invalid emplacement_affichage_id
        emplacement_affichage_id = 10000
        expected_error = {'detail': 'EmplacementAffichage not found'}
        response = self.client.get(f'/emplacementAffichages/{emplacement_affichage_id}')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), expected_error)

if __name__ == '__main__':
    unittest.main()