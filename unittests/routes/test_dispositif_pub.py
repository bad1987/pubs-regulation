import asyncio
from unittest import TestCase
import unittest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
import sys
sys.path.append("../..")

from schemas.DispositifPubSchema import DispositifPubSchema

from models.dispositifs import DispositifPub
from models.typeDispositif import TypeDispositif
from models.tiers import Tiers, TypeTiers
from models.emplacementAffichage import EmplacementAffichage
from models.quartierAffichage import QuartierAffichage
from models.zoneAffichage import ZoneAffichage

from main import app
from db.Connexion import SessionLocal

class TestDispositifPub(TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.db = SessionLocal()
        # Create test data for tiers
        self.type_tiers = TypeTiers(LibelleTypeTiers="Test TypeTiers")
        self.db.add(self.type_tiers)
        self.tiers = Tiers(CodeTiers="Test CodeTiers", LibelleTiers="Test LibelleTiers", AdresseTiers="Test AdresseTiers", TelephoneTiers=691796631, IDTypeTiers=self.type_tiers.IDTypeTiers, NumCont="Test NumCont",EmailTiers="Test EmailTiers", Logo="Test Logo",SigleTiers="Test SigleTiers")
        self.tiers.type_tiers = self.type_tiers
        self.db.add(self.tiers)
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
        # create TypeDispositifPub test data
        self.type_dispositif = TypeDispositif(CodeTypeDispositif="XYZ", LibelleTypeDispo="Test LibelleTypeDispo")
        self.db.add(self.type_dispositif)
        # create DispositifPub test data
        self.dispositif = DispositifPub(CodeDispositifPub="XYZ", LibelleDispoPub="Test LibelleDispoPub", UniteFacturationDispoPub="Test UniteFacturationDispoPub", SurfaceDispoPub=1.0, IDTiers=self.tiers.IDTiers, IDEmplacementAffichage=self.emplacement_affichage.IDEmplacementAffichage, IDTypeDispositif=self.type_dispositif.IDTypeDispositif)
        self.dispositif.type_dispositif = self.type_dispositif
        self.dispositif.tiers = self.tiers
        self.dispositif.emplacement_affichage = self.emplacement_affichage
        self.db.add(self.dispositif)
        self.db.commit()
        self.db.refresh(self.tiers)
        self.db.refresh(self.type_tiers)
    
    def tearDown(self):
        # Remove test data
        Tiers.delete(self.db, self.tiers.IDTiers)
        TypeTiers.delete(self.db, self.type_tiers.IDTypeTiers)
        ZoneAffichage.delete(self.db, self.zone_affichage.IDZoneAffichage)
        QuartierAffichage.delete(self.db, self.quartier_affich.IDQuartierAffichage)
        EmplacementAffichage.delete(self.db, self.emplacement_affichage.IDEmplacementAffichage)
        TypeDispositif.delete(self.db, self.type_dispositif.IDTypeDispositif)
        # DispositifPub.delete(self.db, self.dispositif.IDDispositifPub)
        self.db.commit()
        self.db.close()

    
    def test_get_by_code(self):
        # Test case 1: Valid code
        code_dispositif_pub = self.dispositif.CodeDispositifPub
        response = self.client.get(f'/dispositif/code', params={'CodeDispositifPub': code_dispositif_pub})
        self.assertEqual(response.status_code, 200)
        expected_result = DispositifPubSchema.model_validate(self.dispositif)
        self.assertEqual(response.json(), expected_result.model_dump())

        # Test case 2: Invalid code
        code_dispositif_pub = "ZYX"
        response = self.client.get(f'/dispositif/code', params={'CodeDispositifPub': code_dispositif_pub})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'DispositifPub not found'})

    def test_get_by_id(self):
        # Test case 1: Valid ID
        ID_dispositif_pub = self.dispositif.IDDispositifPub
        response = self.client.get(f'/dispositif/{ID_dispositif_pub}')
        self.assertEqual(response.status_code, 200)
        expected_result = DispositifPubSchema.model_validate(self.dispositif)
        self.assertEqual(response.json(), expected_result.model_dump())

        # Test case 2: Invalid ID
        ID_dispositif_pub = 10000
        response = self.client.get(f'/dispositif/{ID_dispositif_pub}')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'DispositifPub not found'})

    def test_get_all(self):
        response = self.client.get(f'/dispositif')
        self.assertEqual(response.status_code, 200)
        expected_result = DispositifPubSchema.model_validate(self.dispositif)
        self.assertEqual(response.json(), [expected_result.model_dump()])

    def test_create_dispositif_pub(self):
        post_data = {
            "CodeDispositifPub": "LMN",
            "LibelleDispoPub": "Test Create LibelleDispoPub",
            "UniteFacturationDispoPub": "Test Create UniteFacturationDispoPub",
            "SurfaceDispoPub": 1.0,
            "IDTiers": self.tiers.IDTiers,
            "IDEmplacementAffichage": self.emplacement_affichage.IDEmplacementAffichage,
            "IDTypeDispositif": self.type_dispositif.IDTypeDispositif
        }
        response = self.client.post(f'/dispositif', json=post_data)
        self.assertEqual(response.status_code, 201)
        expected_result = self.client.get(f'/dispositif/code', params={'CodeDispositifPub': post_data['CodeDispositifPub']})
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())

        # clean up test data through delete endpoint
        response = self.client.delete(f'/dispositif/{response.json()["IDDispositifPub"]}')
        self.assertEqual(response.status_code, 204)

    def test_update_dispositif(self):
        post_data = {
            "IDDispositifPub": self.dispositif.IDDispositifPub,
            "CodeDispositifPub": self.dispositif.CodeDispositifPub,
            "LibelleDispoPub": "Test Update LibelleDispoPub",
            "UniteFacturationDispoPub": "Test Update UniteFacturationDispoPub",
            "SurfaceDispoPub": 1.0,
            "IDTiers": self.tiers.IDTiers,
            "IDEmplacementAffichage": self.emplacement_affichage.IDEmplacementAffichage,
            "IDTypeDispositif": self.type_dispositif.IDTypeDispositif
        }
        response = self.client.put(f'/dispositif/{self.dispositif.IDDispositifPub}', json=post_data)
        self.assertEqual(response.status_code, 200)
        expected_result = self.client.get(f'/dispositif/{self.dispositif.IDDispositifPub}')
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())

if __name__ == '__main__':
    unittest.main()