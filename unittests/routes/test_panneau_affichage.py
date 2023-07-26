import asyncio
from unittest import TestCase
import unittest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
import sys
sys.path.append("../..")

from schemas.PanneauAffich import PanneauAffichSchema

from models.panneauAffiche import PanneauAffich
from models.typePanneau import TypePanneau
from models.dispositifs import DispositifPub
from models.typeDispositif import TypeDispositif
from models.tiers import Tiers, TypeTiers
from models.emplacementAffichage import EmplacementAffichage
from models.quartierAffichage import QuartierAffichage
from models.zoneAffichage import ZoneAffichage

from main import app
from db.Connexion import SessionLocal

class TestPanneauAffichage(TestCase):
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
        # Create test data for panneau_affich
        self.type_panneau = TypePanneau(CodeTypePanneau="XYZ", LibelleType="Test LibelleType")
        self.db.add(self.type_panneau)
        self.panneau_affich = PanneauAffich(CodeDispositifPub="XYZ", LibelleDispoPub="Test LibelleDispoPub", UniteFacturationDispoPub="Test UniteFacturationDispoPub", SurfaceDispoPub=1.0, IDTiers=self.tiers.IDTiers, IDEmplacementAffichage=self.emplacement_affichage.IDEmplacementAffichage, IDTypeDispositif=self.type_dispositif.IDTypeDispositif, CodePanneau="XYZ", SurfacePanneau=1.0, NbreFacePanneau=1, SpecificiteFact=True, UniteFacturationPanneau="Test Unite", IDTypePanneau=self.type_panneau.IDTypePanneau)
        self.panneau_affich.type_panneau = self.type_panneau
        self.panneau_affich.tiers = self.tiers
        self.panneau_affich.emplacement_affichage = self.emplacement_affichage
        self.panneau_affich.type_dispositif = self.type_dispositif
        self.db.add(self.panneau_affich)
        self.db.commit()
        self.db.refresh(self.panneau_affich)
        self.db.refresh(self.type_panneau)
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
        TypePanneau.delete(self.db, self.type_panneau.IDTypePanneau)
        # PanneauAffich.delete(self.db, self.panneau_affich.IDPanneauAffich)
        self.db.commit()
        self.db.close()

    def test_get_by_code(self):
        # Test case 1: Valid code
        code_panneau = self.panneau_affich.CodePanneau
        response = self.client.get(f"/panneauAffich/code", params={"CodePanneau": code_panneau})
        self.assertEqual(response.status_code, 200)
        exepected_result = PanneauAffichSchema.from_orm(self.panneau_affich)
        self.assertEqual(response.json(), exepected_result.dict())

        # Test case 2: Invalid code
        code_panneau = "ZYX"
        response = self.client.get(f"/panneauAffich/code", params={"CodePanneau": code_panneau})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'PanneauAffich not found'})
    
    def test_get_by_id(self):
        # Test case 1: Valid ID
        id_panneau = self.panneau_affich.IDPanneauAffich
        response = self.client.get(f"/panneauAffich/{id_panneau}")
        self.assertEqual(response.status_code, 200)
        exepected_result = PanneauAffichSchema.from_orm(self.panneau_affich)
        self.assertEqual(response.json(), exepected_result.dict())

        # Test case 2: Invalid ID
        id_panneau = 10000
        response = self.client.get(f"/panneauAffich/{id_panneau}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'PanneauAffich not found'})
    
    def test_get_all(self):
        response = self.client.get("/panneauAffich")
        self.assertEqual(response.status_code, 200)
        expected_result = [PanneauAffichSchema.from_orm(self.panneau_affich).dict()]
        self.assertEqual(response.json(), expected_result)
    
    async def test_create_panneau_affiche(self):
        post_data = {
            "CodeDispositifPub": "LMN",
            "LibelleDispoPub": "Test Create LibelleDispoPub",
            "UniteFacturationDispoPub": "Test Create UniteFacturationDispoPub",
            "SurfaceDispoPub": 1.0,
            "IDTiers": self.tiers.IDTiers,
            "IDTypeDispositif": self.type_dispositif.IDTypeDispositif,
            "CodePanneau": "ABC",
            "SurfacePanneau": 1.0,
            "NbreFacePanneau": 1,
            "SpecificiteFact": True,
            "UniteFacturationPanneau": "Test C Unit",
            "IDTypePanneau": self.type_panneau.IDTypePanneau,
            "IDEmplacementAffichage": self.emplacement_affichage.IDEmplacementAffichage
        }
        response = self.client.post("/panneauAffich", json=post_data)
        self.assertEqual(response.status_code, 201)
        expected_result = self.client.get("/panneauAffich/code", params={"CodePanneau": post_data["CodePanneau"]})
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())

        # clean up through delete endpoint
        response = self.client.delete(f"/panneauAffich/{self.panneau_affich.IDPanneauAffich}")
        self.assertEqual(response.status_code, 204)
    
    def test_update_panneau_affiche(self):
        post_data = {
            "IDPanneauAffich": self.panneau_affich.IDPanneauAffich,
            "CodeDispositifPub": "LMN",
            "LibelleDispoPub": "Test Update LibelleDispoPub",
            "UniteFacturationDispoPub": "Test Update UniteFacturationDispoPub",
            "SurfaceDispoPub": 1.0,
            "IDTiers": self.tiers.IDTiers,
            "IDTypeDispositif": self.type_dispositif.IDTypeDispositif,
            "CodePanneau": self.panneau_affich.CodePanneau,
            "SurfacePanneau": 1.0,
            "NbreFacePanneau": 1,
            "SpecificiteFact": True,
            "UniteFacturationPanneau": "Test U Unit",
            "IDTypePanneau": self.type_panneau.IDTypePanneau,
            "IDEmplacementAffichage": self.emplacement_affichage.IDEmplacementAffichage
        }
        response = self.client.put(f"/panneauAffich/{self.panneau_affich.IDPanneauAffich}", json=post_data)
        self.assertEqual(response.status_code, 200)
        expected_result = self.client.get(f"/panneauAffich/{self.panneau_affich.IDPanneauAffich}")
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())

if __name__ == "__main__":
    unittest.main()