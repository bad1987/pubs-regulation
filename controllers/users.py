import re
from models.users import Permission, User
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from schemas.UserSchema import UserCreateSchema

# a controller to manage users by exploiting the user model
class UserController:
    # a class method to get a user from the database. throws an error if the user does not exist
    @classmethod
    def get(cls, db: Session, user_id: int):
        try:
            user = User.get(db, user_id)
            # if user not found, throw an error
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
            return user
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
    
    # get a user by email
    @classmethod
    def get_user_by_email(cls, db: Session, email: str):
        # first check if the email respect the pattern of a valid email using regex
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email")
        try:
            user = User.get(db, email)
            # if user not found, throw an error
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
            return user
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))
    
    # create a user
    @classmethod
    def create(cls, db: Session, user_data: UserCreateSchema):
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
            user = User(**user_data.model_dump())
            user.set_password(user_data.password)
            for permission_id in user_data.permissions:
                permission = Permission.get(db, permission_id)
                if permission:
                    user.permissions.append(permission)
            user = User.create(db, user)
            return user
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_NOT_FOUND, detail=str(e))