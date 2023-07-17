import unittest
import sys
sys.path.append("..")
from models.panneauAffiche import PanneauAffich
from db.Connexion import Base, SessionLocal
from models.typePanneau import TypePanneau

class TestTypePanneau(unittest.TestCase):
    def setUp(self):
        # Set up the test environment, such as creating a test database or mocking dependencies
        self.db = SessionLocal()  # Replace with your actual test database connection

        # Create some test data
        self.type_panneau = TypePanneau(
            CodeTypePanneau="ABC123",
            LibelleType="Test Type"
        )
        self.db.add(self.type_panneau)
        self.db.commit()

    def tearDown(self):
        # Clean up any resources used in the test, such as closing database connections
        self.db.delete(self.type_panneau)
        self.db.commit()
        self.db.close()  # Replace with your actual cleanup code

    def test_get(self):
        # Test the get method
        type_panneau = TypePanneau.get(self.db, self.type_panneau.IDTypePanneau)
        self.assertEqual(type_panneau.IDTypePanneau, self.type_panneau.IDTypePanneau)

    def test_getAll(self):
        # Test the getAll method
        type_panneaux = TypePanneau.getAll(self.db)
        self.assertGreater(len(type_panneaux), 0)

    def test_getByCode(self):
        # Test the getByCode method
        type_panneau = TypePanneau.getByCode(self.db, self.type_panneau.CodeTypePanneau)
        self.assertEqual(type_panneau.CodeTypePanneau, self.type_panneau.CodeTypePanneau)

    def test_create(self):
        # Test the create method
        new_type_panneau = TypePanneau.create(self.db, TypePanneau(
            CodeTypePanneau="XYZ789",
            LibelleType="New Type"
        ))
        self.assertIsNotNone(new_type_panneau.IDTypePanneau)

        TypePanneau.delete(self.db, new_type_panneau.IDTypePanneau)


    def test_updateLibelleType(self):
        # Test the updateLibelleType method
        updated_type_panneau = TypePanneau.updateLibelleType(self.db, self.type_panneau.IDTypePanneau, "Updated Type")
        self.assertEqual(updated_type_panneau.LibelleType, "Updated Type")

    def test_delete(self):
        # Test the delete method
        result = TypePanneau.delete(self.db, self.type_panneau.IDTypePanneau)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()