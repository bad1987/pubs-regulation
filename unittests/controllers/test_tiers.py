import unittest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from unittest.mock import patch

class TestTiersController(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.client = TestClient(app)

        # Create a mock session
        self.session = Session()

        # Patch the Tiers model methods for testing
        patch('models.tiers.Tiers.get').start()
        patch('models.tiers.Tiers.getAll').start()
        patch('models.tiers.Tiers.getByCode').start()
        patch('models.tiers.Tiers.create').start()
        patch('models.tiers.Tiers.updateNumCont').start()
        patch('models.tiers.Tiers.updateLibelleTiers').start()
        patch('models.tiers.Tiers.updateAdresseTiers').start()
        patch('models.tiers.Tiers.updateSigleTiers').start()
        patch('models.tiers.Tiers.updateLogo').start()
        patch('models.tiers.Tiers.delete').start()

        # Patch the TypeTiers model methods for testing
        patch('models.tiers.TypeTiers.get').start()
        patch('models.tiers.TypeTiers.getAll').start()
        patch('models.tiers.TypeTiers.create').start()
        patch('models.tiers.TypeTiers.delete').start()

    def test_get(self):
        # Test the get method
        ...

    def test_getAll(self):
        # Test the getAll method
        ...

    def test_getByCode(self):
        # Test the getByCode method
        ...

    def test_create(self):
        # Test the create method
        ...

    def test_updateNumCont(self):
        # Test the updateNumCont method
        ...

    def test_updateLibelleTiers(self):
        # Test the updateLibelleTiers method
        ...


    def test_updateAdresseTiers(self):
        # Test the updateAdresseTiers method
        ...

    def test_updateSigleTiers(self):
        # Test the updateSigleTiers method
        ...

    def test_updateLogo(self):
        # Test the updateLogo method
        ...

    def test_delete(self):
        # Test the delete method
        ...

    def test_getTypeTiers(self):
        # Test the getTypeTiers method
        ...

    def test_getAllTypeTiers(self):
        # Test the getAllTypeTiers method
        ...

    def test_createTypeTiers(self):
        # Test the createTypeTiers method
        ...

    def test_deleteTypeTiers(self):
        # Test the deleteTypeTiers method
        ...
