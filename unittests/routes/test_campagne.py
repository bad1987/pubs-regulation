import asyncio
import datetime
from unittest import TestCase
import unittest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
import sys
sys.path.append("../..")
from db.Connexion import SessionLocal
from main import app
from models.tiers import Tiers, TypeTiers
from models.emplacementAffichage import EmplacementAffichage
from models.typeDispositif import TypeDispositif
from models.dispositifs import DispositifPub
from models.produitConcession import ProduitConcession
from models.quartierAffichage import QuartierAffichage
from models.zoneAffichage import ZoneAffichage
from models.campagne import CampagnePub
from models.campagneProduit import CampagneProduit

from schemas.CampagneProduitSchema import CampagnePubSchema
class TestProduitConcession(TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.db = SessionLocal()
        # Create test data for tiers
        self.type_tiers = TypeTiers(LibelleTypeTiers="Test TypeTiers")
        self.db.add(self.type_tiers)
        self.tiers = Tiers(CodeTiers="Test CodeTiers", LibelleTiers="Test LibelleTiers", AdresseTiers="Test AdresseTiers", TelephoneTiers=691796631,
                           IDTypeTiers=self.type_tiers.IDTypeTiers, NumCont="Test NumCont", EmailTiers="Test EmailTiers", Logo="Test Logo", SigleTiers="Test SigleTiers")
        self.tiers.type_tiers = self.type_tiers
        self.db.add(self.tiers)
        # create zoneAffichage test data
        self.zone_affichage = ZoneAffichage(
            CodeZone="ABC", LibelleZone="Test Zone")
        self.db.add(self.zone_affichage)
        # create quartierAffichage test data
        self.quartier_affich = QuartierAffichage(NomQuartier="Test Quartier", SousQuartierAffich="Test Sous Quartier", ObservationsQuartier="Test Observations",
                                                 ArrondissementQuartier="Test Arrondissement", IDZoneAffichage=self.zone_affichage.IDZoneAffichage)
        self.quartier_affich.zone_affichage = self.zone_affichage
        self.db.add(self.quartier_affich)
        # create emplacementAffichage test data
        self.emplacement_affichage = EmplacementAffichage(
            CodeEmplacement="XYZ", IDQuartierAffichage=self.quartier_affich.IDQuartierAffichage)
        self.emplacement_affichage.quartier = self.quartier_affich
        self.db.add(self.emplacement_affichage)
        # create TypeDispositifPub test data
        self.type_dispositif = TypeDispositif(
            CodeTypeDispositif="XYZ", LibelleTypeDispo="Test LibelleTypeDispo")
        self.db.add(self.type_dispositif)
        # create DispositifPub test data
        self.dispositif = DispositifPub(CodeDispositifPub="XYZ", LibelleDispoPub="Test LibelleDispoPub", UniteFacturationDispoPub="Test UniteFacturationDispoPub", SurfaceDispoPub=1.0,
                                        IDTiers=self.tiers.IDTiers, IDEmplacementAffichage=self.emplacement_affichage.IDEmplacementAffichage, IDTypeDispositif=self.type_dispositif.IDTypeDispositif)
        self.dispositif.type_dispositif = self.type_dispositif
        self.dispositif.tiers = self.tiers
        self.dispositif.emplacement_affichage = self.emplacement_affichage
        self.db.add(self.dispositif)
        # create ProduitConcession test data
        self.produit_concession = ProduitConcession(CodeProduitConcession="XYZ", ObservationsProduit="Test ObservationsProduit",
                                                    DureeMinimaleFacturation=1, IDDispositifPub=self.dispositif.IDDispositifPub)
        self.produit_concession.dispositif_pub = self.dispositif
        self.db.add(self.produit_concession)
        # create CampagnePub test data
        self.campagne = CampagnePub(CodeCampagne="XYZ", LibelleCampagne="Test LibelleCampagne", DateDeb=datetime.datetime.utcnow().date().isoformat(), DateFin=datetime.datetime.utcnow().date().isoformat(), SurfaceDispositif=1.0)
        self.campagne.produits.append(self.produit_concession)
        # create campagneProduit test data
        self.campagneProduit = CampagneProduit(IDCampagnePub=self.campagne.IDCampagnePub, IDProduitConcession=self.produit_concession.IDProduitConcession)
        self.db.add(self.campagneProduit)
        self.db.add(self.campagne)
        self.db.commit()
        self.db.refresh(self.tiers)
        self.db.refresh(self.type_tiers)
        self.db.refresh(self.zone_affichage)
        self.db.refresh(self.quartier_affich)
        self.db.refresh(self.emplacement_affichage)
        self.db.refresh(self.type_dispositif)
        self.db.refresh(self.dispositif)
        self.db.refresh(self.produit_concession)
        self.db.refresh(self.campagne)
        self.db.refresh(self.campagneProduit)

    def tearDown(self):
        # Remove test data
        Tiers.delete(self.db, self.tiers.IDTiers)
        TypeTiers.delete(self.db, self.type_tiers.IDTypeTiers)
        ZoneAffichage.delete(self.db, self.zone_affichage.IDZoneAffichage)
        QuartierAffichage.delete(
            self.db, self.quartier_affich.IDQuartierAffichage)
        EmplacementAffichage.delete(
            self.db, self.emplacement_affichage.IDEmplacementAffichage)
        TypeDispositif.delete(self.db, self.type_dispositif.IDTypeDispositif)
        # DispositifPub.delete(self.db, self.dispositif.IDDispositifPub)
        # ProduitConcession.delete(self.db, self.produit_concession.IDProduitConcession)
        CampagnePub.delete(self.db, self.campagne.IDCampagnePub)
        CampagneProduit.delete(self.db, self.campagneProduit.IDCampagneProduit)
        self.db.commit()
        self.db.close()

    def test_get_campagne_by_id(self):
        # Test case 1: Valid campagne_id
        campagne_id = self.campagne.IDCampagnePub
        response = self.client.get(f"/campagne/{campagne_id}")
        expected_result = CampagnePubSchema.model_validate(self.campagne).model_dump()
        print(expected_result)
        expected_result['DateDeb'] = expected_result['DateDeb'].isoformat()
        expected_result['DateFin'] = expected_result['DateFin'].isoformat()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), expected_result)

        # Test case 2: Invalid campagne_id
        campagne_id = 100000
        response = self.client.get(f"/campagne/{campagne_id}")
        self.assertEqual(response.status_code, 404)
        self.assertDictEqual(response.json(), {"detail": "Campagne not found"})

    # def test_get_campagne_by_code(self):
    #     # Test case 1: Valid campagne_code
    #     campagne_code = self.campagne.CodeCampagne
    #     response = self.client.get(f"/campagne/code", params={"CodeCampagne": campagne_code})
    #     expected_result = CampagnePubSchema.model_validate(self.campagne).model_dump()
    #     expected_result['DateDeb'] = expected_result['DateDeb'].isoformat()
    #     expected_result['DateFin'] = expected_result['DateFin'].isoformat()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.json(), expected_result)

    #     # Test case 2: Invalid campagne_code
    #     campagne_code = "ZYX"
    #     response = self.client.get(f"/campagne/code", params={"CodeCampagne": campagne_code})
    #     self.assertEqual(response.status_code, 404)
    #     self.assertDictEqual(response.json(), {"detail": "Campagne not found"})

    # def test_get_all_campagne(self):
    #     response = self.client.get("/campagne")
    #     expected_result = CampagnePubSchema.model_validate(self.campagne).model_dump()
    #     expected_result['DateDeb'] = expected_result['DateDeb'].isoformat()
    #     expected_result['DateFin'] = expected_result['DateFin'].isoformat()
    #     self.assertEqual(response.status_code, 200)
    #     print(response.json())
    #     self.assertListEqual(response.json(), [expected_result])
    
    # def test_create_campagne(self):
    #     post_data = {
    #         "CodeCampagne": "LMN",
    #         "LibelleCampagne": "Test LibelleCampagne",
    #         "DateDeb": datetime.datetime.utcnow().date().isoformat(),
    #         "DateFin": datetime.datetime.utcnow().date().isoformat(),
    #         "SurfaceDispositif": 1.0,
    #         "produits_ids": [self.produit_concession.IDProduitConcession]
    #     }
    #     response = self.client.post("/campagne", json=post_data)
    #     print(response.json())
    #     self.assertEqual(response.status_code, 201)
    #     expected_result = self.client.get(f"/campagne/{response.json()['IDCampagnePub']}")
    #     self.assertEqual(expected_result.status_code, 200)
    #     self.assertDictEqual(expected_result.json(), response.json())

    #     # clean up through delete endpoint
    #     response = self.client.delete(f"/campagne/{response.json()['IDCampagnePub']}")
    #     self.assertEqual(response.status_code, 204)
    
    # def test_update_campagne(self):
    #     modiftime = datetime.datetime.utcnow().date().isoformat()
    #     post_data = {
    #         "IDCampagnePub": self.campagne.IDCampagnePub,
    #         "CodeCampagne": self.campagne.CodeCampagne,
    #         "LibelleCampagne": "Test U LibelleCampagne",
    #         "DateDeb": modiftime,
    #         "DateFin": modiftime,
    #         "SurfaceDispositif": 1.0,
    #     }
    #     response = self.client.put(f"/campagne/{self.campagne.IDCampagnePub}", json=post_data)
    #     self.assertEqual(response.status_code, 200)
    #     expected_result = self.client.get(f"/campagne/{self.campagne.IDCampagnePub}")
    #     self.assertEqual(expected_result.status_code, 200)
    #     self.assertDictEqual(expected_result.json(), response.json())

if __name__ == "__main__":
    unittest.main()