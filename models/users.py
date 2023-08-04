from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, text, BigInteger, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.types import Text
from Enums.UserRoleEnum import UserRoleEnum
from Enums.UserEnums import UserStatusEnum
from Enums.LanguageEnum import LanguageEnum
from db.Connexion import Base
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(255), unique=False, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    firstname = Column(String(255), nullable=True)
    lastname = Column(String(255), nullable=True)
    roles = Column(Enum(UserRoleEnum, values_callable=lambda obj: [e.value for e in obj]), nullable = False)
    status = Column(Enum(UserStatusEnum, values_callable=lambda obj: [e.value for e in obj]), nullable=False)

    permissions = relationship("Permission", secondary='user_permissions', lazy='joined')


    @classmethod
    def get(cls, db: Session, user_id: int) -> 'User':
        return db.query(cls).filter(cls.id == user_id).first()

    @classmethod
    def get_user_by_username(cls, db: Session, username: str) -> 'User':
        return db.query(cls).filter(cls.username == username).first()

    @classmethod
    def get_user_by_email(cls, db: Session, email: str) -> 'User':
        return db.query(cls).filter(cls.email == email).first()

    @classmethod
    def create(cls, db: Session, user) -> 'User':
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    # update
    @classmethod
    def update(cls, db: Session, user: 'User') -> 'User':
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @classmethod
    def delete(cls, db: Session, user_id: int) -> bool:
        user = cls.get(db, user_id)
        if user:
            db.delete(user)
            db.commit()
            return True
        return False
    
    @classmethod
    def add_permission(cls, db: Session, user_id: int, permission_id: int) -> bool:
        user = cls.get(db, user_id)
        permission = Permission.get(db, permission_id)
        if user and permission:
            user.permissions.append(permission)
            db.commit()
            return True
        return False

    @classmethod
    def remove_permission(cls, db: Session, user_id: int, permission_id: int) -> bool:
        user = cls.get(db, user_id)
        permission = Permission.get(db, permission_id)
        if user and permission:
            user.permissions.remove(permission)
            db.commit()
            return True
        return False

    @classmethod
    def has_permission(cls, db: Session, user_id: int, permission_name: str) -> bool:
        user = cls.get(db, user_id)
        if user:
            for permission in user.permissions:
                if permission.name == permission_name:
                    return True
        return False
    
    @classmethod
    def authenticate(cls, db: Session, email: str, password: str) -> 'User':
        user = cls.get_user_by_email(db, email)
        if not user:
            return None
        if not pwd_context.verify(password, user.password):
            return None
        return user

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password)

    def set_password(self, password: str) -> None:
        self.password = pwd_context.hash(password)
    
class Permission(Base):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(25), nullable=False, unique=True) 
    mode = Column(String(25), nullable=False)
    model_name = Column(String(25), nullable=False)
    description = Column(Text, nullable=True)

    @classmethod
    def get(cls, db: Session, permission_id: int):
        return db.query(cls).filter(cls.id == permission_id).first()

    @classmethod
    def create(cls, db: Session, permission):
        db.add(permission)
        db.commit()
        db.refresh(permission)
        return permission

    @classmethod
    def delete(cls, db: Session, permission_id: int):
        permission = cls.get(db, permission_id)
        if permission:
            db.delete(permission)
            db.commit()
            return True
        return False

class User_Permission(Base):
    __tablename__ = "user_permissions"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    permission_id = Column(Integer, ForeignKey("permissions.id", ondelete="CASCADE"), nullable=False)

    @classmethod
    def get(cls, db: Session, user_permission_id: int):
        return db.query(cls).filter(cls.id == user_permission_id).first()
    
    @classmethod
    def getAll(cls, db: Session):
        return db.query(cls).all()

    @classmethod
    def create(cls, db: Session, user_permission):
        db.add(user_permission)
        db.commit()
        db.refresh(user_permission)
        return user_permission

    @classmethod
    def delete(cls, db: Session, user_permission_id: int):
        user_permission = cls.get(db, user_permission_id)
        if user_permission:
            db.delete(user_permission)
            db.commit()
            return True
        return False

class Login_Attempt(Base):
    __tablename__ = "login_attempts"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    ip = Column(String(20), unique=True, nullable=False)
    count = Column(Integer, default=0)
    timestamp = Column(Integer, nullable=True)
