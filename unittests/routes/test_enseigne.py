import asyncio
from unittest import TestCase
import unittest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
import sys
sys.path.append("../..")

from schemas.EnseigneSchema import EnseigneSchema

from models.enseignes import Enseigne
from models.typeEnseigne import TypeEnseigne
from models.dispositifs import DispositifPub
from models.typeDispositif import TypeDispositif
from models.tiers import Tiers, TypeTiers
from models.emplacementAffichage import EmplacementAffichage
from models.quartierAffichage import QuartierAffichage
from models.zoneAffichage import ZoneAffichage

from main import app
from db.Connexion import SessionLocal

class TestEnseigne(TestCase):
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
        # Create test data for enseigne
        self.type_enseigne = TypeEnseigne(CodeTypeEnseigne="XYZ", LibelleTypeEnseigne="Test TypeEnseigne")
        self.db.add(self.type_enseigne)
        self.enseigne = Enseigne(CodeDispositifPub="XYZ", LibelleDispoPub="Test LibelleDispoPub", UniteFacturationDispoPub="Test UniteFacturationDispoPub", SurfaceDispoPub=1.0, IDTiers=self.tiers.IDTiers, IDEmplacementAffichage=self.emplacement_affichage.IDEmplacementAffichage, IDTypeDispositif=self.type_dispositif.IDTypeDispositif, CodeEnseigne="XYZ", SurfaceEnseigne=1.0, NbreFaceEnseigne=1, SpecificiteFacture=True, UniteFacturationEnseigne="Test Unite", IDTypeEnseigne=self.type_enseigne.IDTypeEnseigne)
        self.enseigne.type_enseigne = self.type_enseigne
        self.enseigne.tiers = self.tiers
        self.enseigne.emplacement_affichage = self.emplacement_affichage
        self.enseigne.type_dispositif = self.type_dispositif
        self.db.add(self.enseigne)
        self.db.commit()
        self.db.refresh(self.enseigne)
        self.db.refresh(self.type_enseigne)
        self.db.refresh(self.tiers)
        self.db.refresh(self.type_tiers)
        self.db.refresh(self.zone_affichage)
        self.db.refresh(self.quartier_affich)
        self.db.refresh(self.emplacement_affichage)
        self.db.refresh(self.type_dispositif)
    
    def tearDown(self):
        # Remove test data
        Tiers.delete(self.db, self.tiers.IDTiers)
        TypeTiers.delete(self.db, self.type_tiers.IDTypeTiers)
        ZoneAffichage.delete(self.db, self.zone_affichage.IDZoneAffichage)
        QuartierAffichage.delete(self.db, self.quartier_affich.IDQuartierAffichage)
        EmplacementAffichage.delete(self.db, self.emplacement_affichage.IDEmplacementAffichage)
        TypeDispositif.delete(self.db, self.type_dispositif.IDTypeDispositif)
        # DispositifPub.delete(self.db, self.dispositif.IDDispositifPub)
        TypeEnseigne.delete(self.db, self.type_enseigne.IDTypeEnseigne)
        # Enseigne.delete(self.db, self.enseigne.IDEnseigne)
        self.db.commit()
        self.db.close()

    def test_get_by_code(self):
        # Test case 1: Valid code
        print(jsonable_encoder(self.enseigne))
        code_enseigne = self.enseigne.CodeEnseigne
        response = self.client.get(f"/enseigne/code", params={"CodeEnseigne": code_enseigne})
        self.assertEqual(response.status_code, 200)
        exepected_result = EnseigneSchema.from_orm(self.enseigne)
        self.assertEqual(jsonable_encoder(response.json()), exepected_result.dict())

        # Test case 2: Invalid code
        code_enseigne = "ZYX"
        response = self.client.get(f"/enseigne/code", params={"CodeEnseigne": code_enseigne})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'Enseigne not found'})

    def test_get_by_id(self):
        # Test case 1: Valid ID
        enseigne_id = self.enseigne.IDEnseigne
        response = self.client.get(f"/enseigne/{enseigne_id}")
        self.assertEqual(response.status_code, 200)
        exepected_result = EnseigneSchema.from_orm(self.enseigne)
        self.assertEqual(jsonable_encoder(response.json()), exepected_result.dict())

        # Test case 2: Invalid ID
        enseigne_id = 10000
        response = self.client.get(f"/enseigne/{enseigne_id}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'Enseigne not found'})

    def test_get_all(self):
        response = self.client.get("/enseigne")
        self.assertEqual(response.status_code, 200)
        expected_result = [EnseigneSchema.from_orm(self.enseigne).dict()]
        self.assertEqual(jsonable_encoder(response.json()), expected_result)

    def test_create_enseigne(self):
        post_data = {
            "CodeDispositifPub": "LMN",
            "LibelleDispoPub": "Test Create LibelleDispoPub",
            "UniteFacturationDispoPub": "Test Create UniteFacturationDispoPub",
            "SurfaceDispoPub": 1.0,
            "IDTiers": self.tiers.IDTiers,
            "IDTypeDispositif": self.type_dispositif.IDTypeDispositif,
            "CodeEnseigne": "LMN",
            "SurfaceEnseigne": 1.0,
            "NbreFaceEnseigne": 1,
            "SpecificiteFacture": True,
            "UniteFacturationEnseigne": "Test C Unit",
            "IDTypeEnseigne": self.type_enseigne.IDTypeEnseigne,
            "IDEmplacementAffichage": self.emplacement_affichage.IDEmplacementAffichage
        }
        response = self.client.post("/enseigne", json=post_data)
        self.assertEqual(response.status_code, 201)
        expected_result = self.client.get("/enseigne/code", params={"CodeEnseigne": post_data["CodeEnseigne"]})
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())

        # clean up through delete endpoint
        response = self.client.delete(f"/enseigne/{response.json()['IDEnseigne']}")
        self.assertEqual(response.status_code, 204)

    def test_update_enseigne(self):
        post_data = {
            "IDEnseigne": self.enseigne.IDEnseigne,
            "CodeDispositifPub": self.enseigne.CodeDispositifPub,
            "LibelleDispoPub": "Test Update LibelleDispoPub",
            "UniteFacturationDispoPub": "Test Update UniteFacturationDispoPub",
            "SurfaceDispoPub": 1.0,
            "IDTiers": self.tiers.IDTiers,
            "IDTypeDispositif": self.type_dispositif.IDTypeDispositif,
            "CodeEnseigne": self.enseigne.CodeEnseigne,
            "SurfaceEnseigne": 1.0,
            "NbreFaceEnseigne": 1,
            "SpecificiteFacture": True,
            "UniteFacturationEnseigne": "Test U Unit",
            "IDTypeEnseigne": self.type_enseigne.IDTypeEnseigne,
            "IDEmplacementAffichage": self.emplacement_affichage.IDEmplacementAffichage
        }
        response = self.client.put(f"/enseigne/{self.enseigne.IDEnseigne}", json=post_data)
        self.assertEqual(response.status_code, 200)
        expected_result = self.client.get(f"/enseigne/{self.enseigne.IDEnseigne}")
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())

if __name__ == "__main__":
    unittest.main()