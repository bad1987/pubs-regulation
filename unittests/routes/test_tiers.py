import asyncio
from unittest import TestCase
import unittest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
import sys
sys.path.append("../..")

from schemas.TiersSchema import TiersSchema

from models.tiers import Tiers, TypeTiers

from main import app
from db.Connexion import SessionLocal

class TestTiers(TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.db = SessionLocal()
        # Create test data for tiers
        self.type_tiers = TypeTiers(LibelleTypeTiers="Test TypeTiers")
        self.db.add(self.type_tiers)
        self.tiers = Tiers(CodeTiers="Test CodeTiers", LibelleTiers="Test LibelleTiers", AdresseTiers="Test AdresseTiers", TelephoneTiers=691796631, IDTypeTiers=self.type_tiers.IDTypeTiers, NumCont="Test NumCont",EmailTiers="Test EmailTiers", Logo="Test Logo",SigleTiers="Test SigleTiers")
        self.tiers.type_tiers = self.type_tiers
        self.db.add(self.tiers)
        self.db.commit()
        self.db.refresh(self.tiers)
        self.db.refresh(self.type_tiers)
    
    def tearDown(self):
        # Remove test data
        Tiers.delete(self.db, self.tiers.IDTiers)
        TypeTiers.delete(self.db, self.type_tiers.IDTypeTiers)
        self.db.commit()
        self.db.close()
    
    def test_get_tiers_by_id(self):
        # Test case 1: Valid tiers_id
        tiers_id = self.tiers.IDTiers
        expected_result = TiersSchema(**jsonable_encoder(self.tiers))
        response = self.client.get(f'/tiers/{tiers_id}')
        print(response.json())
        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(), expected_result.model_dump())

        # Test case 2: Invalid tiers_id
        tiers_id = 1000000
        expected_error = {'detail': 'Tiers not found'}
        response = self.client.get(f'/tiers/{tiers_id}')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), expected_error)
    
    # test get all
    def test_get_all_tiers(self):
        expected_result = [TiersSchema(**jsonable_encoder(self.tiers)).model_dump()]
        response = self.client.get('/tiers')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result)
    
    # test the post route
    def test_create_tiers(self):
        # create test data
        post_data = {
            "CodeTiers": "Create Test CodeTiers",
            "LibelleTiers": "Create Test LibelleTiers",
            "AdresseTiers": "Create Test AdresseTiers",
            "TelephoneTiers": 691796631,
            "IDTypeTiers": self.type_tiers.IDTypeTiers,
            "NumCont": "Create Test NumCont",
            "EmailTiers": "Create Test EmailTiers",
            "Logo": "Create Test Logo",
            "SigleTiers": "Create Test SigleTiers"
        }
        response = self.client.post('/tiers', json=post_data)
        self.assertEqual(response.status_code, 201)
        expected_result = self.client.get(f'/tiers/{response.json()["IDTiers"]}')
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())

        # clean up
        response = self.client.delete(f'/tiers/{self.tiers.IDTiers}')
        self.assertEqual(response.status_code, 204)

    # test the put route
    def test_update_tiers(self):
        # create test data
        put_data = {
            "IDTiers": self.tiers.IDTiers,
            "CodeTiers": "Update Test CodeTiers",
            "LibelleTiers": "Update Test LibelleTiers",
            "AdresseTiers": "Update Test AdresseTiers",
            "TelephoneTiers": 691796631,
            "IDTypeTiers": self.type_tiers.IDTypeTiers,
            "NumCont": "Update Test NumCont",
            "EmailTiers": "Update Test EmailTiers",
            "Logo": "Update Test Logo",
            "SigleTiers": "Update Test SigleTiers"
        }
        response = self.client.put(f'/tiers/{self.tiers.IDTiers}', json=put_data)
        self.assertEqual(response.status_code, 200)
        expected_result = self.client.get(f'/tiers/{self.tiers.IDTiers}')
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())


if __name__ == '__main__':
    unittest.main()
