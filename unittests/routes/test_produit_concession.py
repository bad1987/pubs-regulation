import asyncio
import datetime
from unittest import TestCase
import unittest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
import sys
sys.path.append("../..")

from models.quartierAffichage import QuartierAffichage
from models.zoneAffichage import ZoneAffichage

from schemas.ProduitConsession import ProduitConsessionSchema

from models.produitConcession import ProduitConcession
from models.dispositifs import DispositifPub
from models.typeDispositif import TypeDispositif
from models.emplacementAffichage import EmplacementAffichage
from models.tiers import Tiers, TypeTiers

from main import app
from db.Connexion import SessionLocal

class TestProduitConcession(TestCase):
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
        # create ProduitConcession test data
        self.produit_concession = ProduitConcession(CodeProduitConcession="XYZ", ObservationsProduit="Test ObservationsProduit", DureeMinimaleFacturation=1, IDDispositifPub=self.dispositif.IDDispositifPub)
        self.produit_concession.dispositif_pub = self.dispositif
        self.db.add(self.produit_concession)
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
        ProduitConcession.delete(self.db, self.produit_concession.IDProduitConcession)
        self.db.commit()
        self.db.close()

if __name__ == '__main__':
    unittest.main()