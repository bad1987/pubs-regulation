import re
from models.users import Permission, User
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from schemas.UserSchema import UserCreateSchema, UserSchema, UserUpdateSchema

# a controller to manage users by exploiting the user model
class UserController:
    # a class method to get a user from the database. throws an error if the user does not exist
    @classmethod
    def get(cls, db: Session, user_id: int) -> UserSchema:
        try:
            user = User.get(db, user_id)
            # if user not found, throw an error
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
            return UserSchema.model_validate(user)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # get a user by email
    @classmethod
    def get_user_by_email(cls, db: Session, email: str) -> UserSchema:
        # first check if the email respect the pattern of a valid email using regex
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email")
        try:
            user = User.get_user_by_email(db, email)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
        # if user not found, throw an error
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return UserSchema.model_validate(user)
    
    # create a user
    @classmethod
    def create(cls, db: Session, user_data: UserCreateSchema) -> UserSchema:
        # validate username(should not be empty) and email
        if not re.match(r"[^@]+@[^@]+\.[^@]+", user_data.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email")
        if not user_data.username:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A username is required")
        # password should not be empty
        if not user_data.password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A password is required")
        # check if the user already exists with the same email or username
        if User.get_user_by_email(db, user_data.email) or User.get_user_by_username(db, user_data.username):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
        try:
            user = User(**user_data.model_dump(exclude={"permissions"}))
            user.set_password(user_data.password)
            for permission_id in user_data.permissions:
                permission = Permission.get(db, permission_id)
                if permission:
                    user.permissions.append(permission)
            user = User.create(db, user)
            return UserSchema.model_validate(user)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # update a user
    @classmethod
    def update(cls, db: Session, IDUser: int, updateUser: UserUpdateSchema) -> UserSchema:
        # if user does not exist, throw an error
        try:
            user = User.get(db, IDUser)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        try:
            update_data = updateUser.model_dump(exclude_unset=True)
            for key,value in update_data.items():
                setattr(user, key,value)
            user = User.update(db, user)
            return UserSchema.model_validate(user)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

    # delete a user
    @classmethod
    def delete(cls, db: Session, user_id: int) -> bool:
        # if user does not exist, throw an error
        user = User.get(db, user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        try:
            return User.delete(db, user_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # get a user by username
    @classmethod
    def get_user_by_username(cls, db: Session, username: str) -> UserSchema:
        # if user does not exist, throw an error
        user = User.get_user_by_username(db, username)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return UserSchema.model_validate(user)
    
    # add a permission to a user
    @classmethod
    def add_permission(cls, db: Session, user_id: int, permission_id: int) -> bool:
        # if user does not exist, throw an error
        user = User.get(db, user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        # if permission does not exist, throw an error
        permission = Permission.get(db, permission_id)
        if not permission:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permission not found")
        try:
            return User.add_permission(db, user_id, permission_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
    # remove a permission from a user
    @classmethod
    def remove_permission(cls, db: Session, user_id: int, permission_id: int) -> bool:
        # if user does not exist, throw an error
        user = User.get(db, user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        # if permission does not exist, throw an error
        permission = Permission.get(db, permission_id)
        if not permission:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Permission not found")
        try:
            return User.remove_permission(db, user_id, permission_id)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        