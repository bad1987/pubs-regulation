import datetime
from unittest import TestCase
import unittest
import sys
from Enums.UserEnums import UserStatusEnum
from Enums.UserRoleEnum import UserRoleEnum
sys.path.append("../..")
from db.Connexion import SessionLocal

from models.users import Permission, User
 
from schemas.UserSchema import UserCreateSchema, UserSchema, UserUpdateSchema

from controllers.users import UserController

class UserControllerTest(TestCase):
    def setUp(self):
        self.db = SessionLocal()
        # Create test data for user
        self.permission = Permission(
            name="user_permission", mode="read", description="user read test permission", model_name="User"
        )
        self.db.add(self.permission)
        self.user = User(
            email="test@test.com", username="test", password="test", firstname="Test", lastname="Test", roles=UserRoleEnum.ADMIN.value, status=UserStatusEnum.ACTIVE.value
        )
        self.user.permissions.append(self.permission)
        self.db.add(self.user)
        self.db.commit()
        self.db.refresh(self.permission)
        self.db.refresh(self.user)
    
    def tearDown(self):
        User.delete(self.db, self.user.id)
        Permission.delete(self.db, self.permission.id)
        self.db.close()
    
    def test_get_user_by_id(self):
        # Test case 1: valid user_id
        user_id = self.user.id
        user = UserController.get(self.db, user_id).model_dump()
        expected_result = UserSchema.model_validate(self.user).model_dump()
        self.assertEqual(user, expected_result)

    def test_get_user_by_username(self):
        # Test case 1: valid user_username
        user_username = self.user.username
        user = UserController.get_user_by_username(self.db, user_username).model_dump()
        expected_result = UserSchema.model_validate(self.user).model_dump()
        self.assertEqual(user, expected_result)
    
    def test_get_user_by_email(self):
        # Test case 1: valid email
        user_email = 'test@test.com'
        user = UserController.get_user_by_email(self.db, user_email).model_dump()
        expected_result = UserSchema.model_validate(self.user).model_dump()
        self.assertEqual(user, expected_result)

if __name__ == "__main__":
    unittest.main()