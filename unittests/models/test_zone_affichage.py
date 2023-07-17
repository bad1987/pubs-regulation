import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
import sys
sys.path.append("../..")
from db.Connexion import SessionLocal
from models.dispositifs import DispositifPub
from models.emplacementAffichage import EmplacementAffichage
from models.zoneAffichage import ZoneAffichage
from models.quartierAffichage import QuartierAffichage

class TestZoneAffichage(unittest.TestCase):
    def setUp(self):
        self.db = MagicMock(spec=Session)

    def tearDown(self):
        self.db.query.return_value.filter.return_value.delete.return_value = None
        self.db.commit.return_value = None

    def test_get(self):
        # Create test data
        codeZone = "ABC"
        zoneAffichage = ZoneAffichage(CodeZone=codeZone)
        self.db.query.return_value.filter.return_value.first.return_value = zoneAffichage

        # Call the method being tested
        result = ZoneAffichage.get(self.db, codeZone)

        # Assert the expected result
        self.assertEqual(result, zoneAffichage)
        self.db.query.assert_called_once_with(ZoneAffichage)
        self.assertEqual(result.CodeZone, codeZone)
        self.db.query.return_value.filter.return_value.first.assert_called_once()


    def test_getByCodeZone(self):
        # Create test data
        codeZone = 'ABC'
        zoneAffichage = ZoneAffichage(CodeZone=codeZone)
        self.db.query.return_value.filter.return_value.first.return_value = zoneAffichage

        # Call the method being tested
        result = ZoneAffichage.getByCodeZone(self.db, codeZone)
        # Assert the expected result
        self.assertEqual(result, zoneAffichage)
        self.db.query.assert_called_once_with(ZoneAffichage)
        self.assertEqual(result.CodeZone, codeZone)

    def test_create(self):
        # Create test data
        zoneAffichage = ZoneAffichage()

        # Call the method being tested
        result = ZoneAffichage.create(self.db, zoneAffichage)

        # Assert the expected result
        self.assertEqual(result, zoneAffichage)
        self.db.add.assert_called_once_with(zoneAffichage)
        self.db.commit.assert_called_once()
        self.db.refresh.assert_called_once_with(zoneAffichage)

    def test_delete(self):
        # Create test data
        codeZone = 'ABC'
        zoneAffichage = ZoneAffichage(CodeZone=codeZone)
        self.db.query.return_value.filter.return_value.first.return_value = zoneAffichage

        # Call the method being tested
        result = ZoneAffichage.delete(self.db, zoneAffichage.IDZoneAffichage)

        # Assert the expected result
        self.assertTrue(result)
        self.db.query.assert_called_once_with(ZoneAffichage)
        self.db.delete.assert_called_once_with(zoneAffichage)
        self.db.commit.assert_called_once()

    # def test_getAllByQuartiers(self):
    #     # Create test data
    #     codeZone = 'ABC'
    #     zoneAffichage = ZoneAffichage(CodeZone=codeZone)
    #     self.db.query.return_value.filter.return_value.all.return_value = [zoneAffichage]

    #     # Call the method being tested
    #     result = ZoneAffichage.getAllByQuartiers(self.db, quartier_id)

    #     # Assert the expected result
    #     self.assertEqual(result, [zoneAffichage])
    #     self.db.query.assert_called_once_with(ZoneAffichage)
    #     self.db.query.return_value.filter.assert_called_once_with(ZoneAffichage.quartiers.any(quartier_id))
    #     self.db.query.return_value.filter.return_value.all.assert_called_once()

    def test_update(self):
        # Create test data
        codeZone = 'ABC'
        new_data = {"CodeZone": "XYZ"}
        zoneAffichage = ZoneAffichage(CodeZone=codeZone)
        self.db.query.return_value.filter.return_value.first.return_value = zoneAffichage

        # Call the method being tested
        result = ZoneAffichage.update_libelle_zone(self.db, zoneAffichage.IDZoneAffichage, new_data['CodeZone'])

        # Assert the expected result
        zoneAffichage = ZoneAffichage.get(self.db, zoneAffichage.IDZoneAffichage)
        self.assertEqual(result, zoneAffichage)
        self.assertEqual(zoneAffichage.LibelleZone, result.LibelleZone)

    def test_getAll(self):
        # Create test data
        zoneAffichage1 = ZoneAffichage(CodeZone="ABC")
        zoneAffichage2 = ZoneAffichage(CodeZone="EFG")
        self.db.query.return_value.all.return_value = [zoneAffichage1, zoneAffichage2]

        # Call the method being tested
        result = ZoneAffichage.getAll(self.db)

        # Assert the expected result
        self.assertEqual(result, [zoneAffichage1, zoneAffichage2])
        self.db.query.assert_called_once_with(ZoneAffichage)
        self.db.query.return_value.all.assert_called_once()


if __name__ == '__main__':
    unittest.main()
