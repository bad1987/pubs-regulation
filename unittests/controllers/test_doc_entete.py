import datetime
from unittest import TestCase
import unittest
import sys
sys.path.append("../..")
from db.Connexion import SessionLocal

from models.docentete import DocEntete
from models.tiers import Tiers, TypeTiers

from controllers.docentete import DocEnteteController

from schemas.DocEnteteSchema import DocEnteteSchema, DocEnteteCreateSchema, DocEnteteUpdateSchema

class DocEnteteControllerTest(TestCase):
    def setUp(self):
        self.db = SessionLocal()
        # Create test data for tiers
        self.type_tiers = TypeTiers(LibelleTypeTiers="Test TypeTiers")
        self.db.add(self.type_tiers)
        self.tiers = Tiers(CodeTiers="Test CodeTiers", LibelleTiers="Test LibelleTiers", AdresseTiers="Test AdresseTiers", TelephoneTiers=691796631,
                            IDTypeTiers=self.type_tiers.IDTypeTiers, NumCont="Test NumCont", EmailTiers="Test EmailTiers", Logo="Test Logo", SigleTiers="Test SigleTiers")
        self.tiers.type_tiers = self.type_tiers
        self.db.add(self.tiers)
        # create docentete test data
        self.doc_entete = DocEntete(
            TypeDocEntete=1, StatutDoc="AV", PenalitesDoc=1, MontantHTDoc=1.0, MontantTaxeDoc=1.0, MontantTTCDoc=1.0
        )
        self.doc_entete.tiers = self.tiers
        self.doc_entete = DocEntete.create(self.db, self.doc_entete)
    
    def tearDown(self):
        TypeTiers.delete(self.db, self.type_tiers.IDTypeTiers)

        self.db.close()
    
    def test_get_docentete_by_id(self):
        # test case 1: valid doc_entete_id
        doc_entete_id = self.doc_entete.IDDocEntete
        expected_result = DocEnteteSchema.model_validate(self.doc_entete).model_dump()
        response = DocEnteteController.get(self.db, doc_entete_id)
        self.assertEqual(response.model_dump(), expected_result)
    
    def test_get_docentete_by_num_doc_entete(self):
        # test case 2: valid doc_entete_num_doc_entete
        doc_entete_num_doc_entete = self.doc_entete.NumDocEntete
        expected_result = DocEnteteSchema.model_validate(self.doc_entete).model_dump()
        response = DocEnteteController.getByNumDocEntete(self.db, doc_entete_num_doc_entete)
        self.assertEqual(response.model_dump(), expected_result)
    
    def test_get_all_docentete(self):
        # test case 3: all docentete
        expected_result = [DocEnteteSchema.model_validate(self.doc_entete).model_dump()]
        response = [DocEnteteSchema.model_validate(doc_entete).model_dump() for doc_entete in DocEnteteController.getAll(self.db)]
        self.assertEqual(response, expected_result)
    
    def test_create_docentete(self):
        # test case 4: valid doc_entete
        create_schema = DocEnteteCreateSchema(
            TypeDocEntete=1, DateDocEntete=datetime.datetime.utcnow().isoformat(), StatutDoc="AV", PenalitesDoc=1, MontantHTDoc=1.0, MontantTaxeDoc=1.0, MontantTTCDoc=1.0,
            IDTiers=self.tiers.IDTiers
        )
        response = DocEnteteController.create(self.db, create_schema)
        # assert response is a DocEnteteSchema
        self.assertIsInstance(response, DocEnteteSchema)

        # clean up 
        response = DocEnteteController.delete(self.db, response.IDDocEntete)
        self.assertTrue(response)
    
    def test_update_docentete(self):
        # test case 5: valid doc_entete
        update_schema = DocEnteteUpdateSchema(
            TypeDocEntete=1, StatutDoc="VA", PenalitesDoc=1, MontantHTDoc=1.0, MontantTaxeDoc=1.0, MontantTTCDoc=1.0,
            IDTiers=self.tiers.IDTiers,
            IDDocEntete=self.doc_entete.IDDocEntete,
            NumDocEntete=self.doc_entete.NumDocEntete
        )
        response = DocEnteteController.update(self.db, self.doc_entete.IDDocEntete, update_schema)
        # assert response is a DocEnteteSchema
        self.assertIsInstance(response, DocEnteteSchema)
        # assert StatutDoc is updated
        self.assertEqual(response.StatutDoc, update_schema.StatutDoc)

if __name__ == '__main__':
    unittest.main()
