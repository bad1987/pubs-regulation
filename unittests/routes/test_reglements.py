import asyncio
import datetime
from unittest import TestCase
import unittest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
import sys
sys.path.append("../..")

from schemas.ReglementSchema import ReglementSchema

from models.tiers import Tiers, TypeTiers
from models.docentete import DocEntete
from models.reglements import Reglement

from main import app
from db.Connexion import SessionLocal

class TestTiers(TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.db = SessionLocal()
        # creata type tiers
        self.type_tiers = TypeTiers(LibelleTypeTiers="test TypeTiers")
        self.db.add(self.type_tiers)
        # creata tiers
        self.tiers = Tiers(CodeTiers="Test CodeTiers", LibelleTiers="Test LibelleTiers", AdresseTiers="Test AdresseTiers", TelephoneTiers=691796631, IDTypeTiers=self.type_tiers.IDTypeTiers, NumCont="Test NumCont",EmailTiers="Test EmailTiers", Logo="Test Logo",SigleTiers="Test SigleTiers")
        self.tiers.type_tiers = self.type_tiers
        self.db.add(self.tiers)
        # create doc entete
        self.doc_entete = DocEntete(TypeDocEntete=1, NumDocEntete="Test NumDocEntete", DateDocEntete=datetime.datetime.now(), MontantHTDoc=1000, MontantTaxeDoc=0, MontantTTCDoc=0, StatutDoc="AV", PenalitesDoc=0, IDTiers=self.tiers.IDTiers)
        self.doc_entete.tiers = self.tiers
        self.db.add(self.doc_entete)
        # create reglement
        self.reglement = Reglement(NumReglt="Test NumReglt", DateReglt=datetime.datetime.now(), MontantRegle=1000, SoldeRglt=0, StatutRglt="AC", ModeRglt="Test ModeRglt", IDDocEntete=self.doc_entete.IDDocEntete)
        self.db.add(self.reglement)
        self.db.commit()
        self.db.refresh(self.reglement)
        self.db.refresh(self.doc_entete)
        self.db.refresh(self.tiers)
        self.db.refresh(self.type_tiers)
    
    def tearDown(self):
        # remove test data
        Tiers.delete(self.db, self.tiers.IDTiers)
        TypeTiers.delete(self.db, self.type_tiers.IDTypeTiers)
        DocEntete.delete(self.db, self.doc_entete.IDDocEntete)
        Reglement.delete(self.db, self.reglement.IDReglement)
        self.db.commit()
        self.db.close()

    def test_get_tiers_by_id(self):
        # test case 1: valid reglement_id
        reglement_id = self.reglement.IDReglement
        expected_result = ReglementSchema(**jsonable_encoder(self.reglement))
        response = self.client.get(f'/reglements/{reglement_id}')
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result.dict())

        # test case 2: invalid reglement_id
        reglement_id = 1000000
        expected_error = {'detail': 'Reglement not found'}
        response = self.client.get(f'/reglements/{reglement_id}')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), expected_error)

if __name__ == '__main__':
    unittest.main()