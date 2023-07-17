import unittest
from sqlalchemy.orm import Session
import sys
sys.path.append('../..')
from db.Connexion import SessionLocal
from models.docentete import DocEntete
from models.taxTiers import TaxTiers
from models.taxTiersDocEntete import TaxTiersDocEntete
from models.produitConcession import ProduitConcession
from models.dispositifs import DispositifPub
from models.tiers import TypeTiers, Tiers

class TestTypeTiers(unittest.TestCase):
    def setUp(self):
        # Set up a test session and create test data
        self.db = SessionLocal()  # Replace with your own session creation logic
        self.type_tiers = TypeTiers(LibelleTypeTiers="Test Type Tiers")
        self.db.add(self.type_tiers)
        self.db.commit()

    def tearDown(self):
        # Clean up the test data
        self.db.delete(self.type_tiers)
        self.db.commit()
        self.db.close()

    def test_get(self):
        # Test the get method
        retrieved_type_tiers = TypeTiers.get(self.db, self.type_tiers.IDTypeTiers)
        self.assertEqual(retrieved_type_tiers, self.type_tiers)

    def test_get_all(self):
        # Test the getAll method
        all_type_tiers = TypeTiers.getAll(self.db)
        self.assertIn(self.type_tiers, all_type_tiers)

    def test_create(self):
        # Test the create method
        new_type_tiers = TypeTiers(LibelleTypeTiers="New Type Tiers")
        created_type_tiers = TypeTiers.create(self.db, new_type_tiers)
        retrieved_type_tiers = TypeTiers.get(self.db, created_type_tiers.IDTypeTiers)
        self.assertEqual(retrieved_type_tiers, created_type_tiers)

        # clean up
        self.db.delete(created_type_tiers)

    # Add more test methods for other methods in the TypeTiers class

class TestTiers(unittest.TestCase):
    def setUp(self):
        # Set up a test session and create test data
        self.db = SessionLocal()  # Replace with your own session creation logic
        self.type_tiers = TypeTiers(LibelleTypeTiers="Test Type Tiers")
        self.tiers = Tiers(CodeTiers="Test Code", LibelleTiers="Test Tiers")
        self.tiers.type_tiers = self.type_tiers
        self.db.add(self.type_tiers)
        self.db.add(self.tiers)
        self.db.commit()

    def tearDown(self):
        # Clean up the test data
        self.db.delete(self.tiers)
        self.db.delete(self.type_tiers)
        self.db.commit()
        self.db.close()

    def test_get(self):
        # Test the get method
        retrieved_tiers = Tiers.get(self.db, self.tiers.IDTiers)
        self.assertEqual(retrieved_tiers, self.tiers)

    def test_get_by_code(self):
        # Test the getByCode method
        retrieved_tiers = Tiers.getByCode(self.db, self.tiers.CodeTiers)
        self.assertEqual(retrieved_tiers, self.tiers)

    def test_get_all(self):
        # Test the getAll method
        all_tiers = Tiers.getAll(self.db)
        self.assertIn(self.tiers, all_tiers)

    def test_create(self):
        # Test the create method
        new_tiers = Tiers(CodeTiers="New Code", LibelleTiers="New Tiers")
        new_type_tiers = TypeTiers(LibelleTypeTiers="New Type Tiers")
        # new_type_tiers = TypeTiers.create(self.db, new_type_tiers)
        new_tiers.type_tiers = new_type_tiers
        created_tiers = Tiers.create(self.db, new_tiers)
        retrieved_tiers = Tiers.get(self.db, created_tiers.IDTiers)
        self.assertEqual(retrieved_tiers, created_tiers)

        # clean up
        self.db.delete(created_tiers)

    # Add more test methods for other methods in the Tiers class

if __name__ == "__main__":
    unittest.main()