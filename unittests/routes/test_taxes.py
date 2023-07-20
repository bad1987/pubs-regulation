import asyncio
from unittest import TestCase
import unittest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
import sys
sys.path.append("../..")

from models.taxes import Taxes
from schemas.TaxesSchema import TaxesSchema

from main import app
from db.Connexion import SessionLocal

class TestTaxes(TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.db = SessionLocal()

        # Create test data
        self.tax_1 = Taxes(CodeTaxe="ABC", LibelleTaxe="Test Tax", TauxTaxe=100)
        self.db.add(self.tax_1)
        self.db.commit()
        self.db.refresh(self.tax_1)

    def tearDown(self):
        # Remove test data
        Taxes.delete(self.db, self.tax_1.IDTaxes)
        self.db.commit()
        self.db.close()

    def test_get_tax_by_id(self):
        # Test case 1: Valid tax_id
        tax_id = self.tax_1.IDTaxes
        # expected_result = Taxes(IDTaxes=self.tax_1.IDTaxes, CodeTaxe=self.tax_1.CodeTaxe, LibelleTaxe=self.tax_1.LibelleTaxe, TauxTaxe=self.tax_1.TauxTaxe)
        expected_result = TaxesSchema(**jsonable_encoder(self.tax_1))
        response = self.client.get(f'/taxes/{tax_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_result.dict())

        # Test case 2: Invalid tax_id
        tax_id = 1
        expected_error = {'detail': 'Tax not found'}
        response = self.client.get(f'/taxes/{tax_id}')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), expected_error)

    def test_get_all_taxes(self):
        # Create test data
        tax_1 = Taxes(CodeTaxe="DEF", LibelleTaxe="Test Tax 1", TauxTaxe=100)
        tax_2 = Taxes(CodeTaxe="GHI", LibelleTaxe="Test Tax 2", TauxTaxe=200)
        self.db.add(tax_1)
        self.db.add(tax_2)
        self.db.commit()
        self.db.refresh(tax_1)
        self.db.refresh(tax_2)

        # Get all taxes
        response = self.client.get("/taxes")
        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check that the response contains two lists
        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), 3)

        # Delete test data
        Taxes.delete(self.db, tax_1.IDTaxes)
        Taxes.delete(self.db, tax_2.IDTaxes)

    def test_get_tax_by_code(self):
        # Create test data
        tax_1 = Taxes(CodeTaxe="DEF", LibelleTaxe="Test Tax 1", TauxTaxe=100)
        self.db.add(tax_1)
        self.db.commit()
        self.db.refresh(tax_1)

        # Get tax by code
        response = self.client.get(f"/taxes/code/{tax_1.CodeTaxe}")

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check the response content
        expected_result = TaxesSchema(**jsonable_encoder(tax_1))
        self.assertEqual(response.json(), expected_result.dict())

        # Delete test data
        Taxes.delete(self.db, tax_1.IDTaxes)

        # Get tax by invalid code
        response = self.client.get("/taxes/code/123")

        # Check the response status code
        self.assertEqual(response.status_code, 404)

        # Check the response content
        expected_error = {'detail': 'Tax not found'}
        self.assertEqual(response.json(), expected_error)

    def test_create_tax(self):
        # Create test data
        tax_data = {
            "CodeTaxe": "NEWDEF",
            "LibelleTaxe": "Test Tax 1",
            "TauxTaxe": 100,
        }
        response = self.client.post("/taxes", json=tax_data)
        # Check the response status code
        self.assertEqual(response.status_code, 201)

        # Check the response content
        expected_result = self.client.get(f"/taxes/code/{tax_data['CodeTaxe']}")
        self.assertEqual(response.json(), expected_result.json())

        # Check that the tax was created in the database
        tax = TaxesSchema.from_orm(response.json())
        self.assertIsNotNone(tax)
        self.assertEqual(tax.CodeTaxe, tax_data["CodeTaxe"])
        self.assertEqual(tax.LibelleTaxe, tax_data["LibelleTaxe"])
        self.assertEqual(tax.TauxTaxe, tax_data["TauxTaxe"])

        # Delete test data
        Taxes.delete(self.db, tax.IDTaxes)

if __name__ == '__main__':
    unittest.main()