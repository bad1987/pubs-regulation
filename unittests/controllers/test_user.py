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
        self.user.set_password(self.user.password)
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
        print(user)
        self.assertEqual(user, expected_result)
    
    def test_get_user_by_email(self):
        # Test case 1: valid email
        user_email = 'test@test.com'
        user = UserController.get_user_by_email(self.db, user_email).model_dump()
        expected_result = UserSchema.model_validate(self.user).model_dump()
        self.assertEqual(user, expected_result)
    
    def test_create_user(self):
        create_schema = UserCreateSchema(
            username="test_create",
            email="test_create@test.com",
            password="test_create",
            firstname="test_create_first",
            lastname="test_create_last",
            status=UserStatusEnum.ACTIVE.value,
            permissions=[self.permission.id],
            roles=UserRoleEnum.ADMIN.value
        )
        user = UserController.create(self.db, create_schema)
        # assert result not None
        self.assertIsNotNone(user)
        # assert response is type UserSchema
        self.assertIsInstance(user, UserSchema)
        # assert username
        self.assertEqual(user.username, create_schema.username)
        # assert email
        self.assertEqual(user.email, create_schema.email)

        # clean up
        response = UserController.delete(self.db, user.id)
        self.assertTrue(response)

    
    def test_update_user(self):
        update_data = UserUpdateSchema(
            status=UserStatusEnum.INACTIVE.value,
            firstname="test_update_first",
            lastname="test_update_last"
        )
        user = UserController.update(self.db, self.user.id, update_data)
        # assert result not None
        self.assertIsNotNone(user)
        # assert response is type UserSchema
        self.assertIsInstance(user, UserSchema)
        # assert status
        self.assertEqual(user.status, update_data.status)
        # assert firstname
        self.assertEqual(user.firstname, update_data.firstname)
        # assert lastname
        self.assertEqual(user.lastname, update_data.lastname)
    
    def test_add_remove_permission(self):
        # create new permission for write permission
        permission = Permission(
            name="user_write_permission", mode="write", description="user write test permission", model_name="User"
        )
        permission = Permission.create(self.db, permission)
        response = UserController.add_permission(self.db, self.user.id, permission.id)
        self.assertTrue(response)
        # assert user permissions
        user = UserController.get(self.db, self.user.id).model_dump()
        self.assertEqual(len(user['permissions']), 2)

        # remove permission
        response = UserController.remove_permission(self.db, self.user.id, permission.id)
        self.assertTrue(response)
        # assert user permissions
        user = UserController.get(self.db, self.user.id).model_dump()
        self.assertEqual(len(user['permissions']), 1)

        # clean up new permission
        response = Permission.delete(self.db, permission.id)
        self.assertTrue(response)


if __name__ == "__main__":
    unittest.main()