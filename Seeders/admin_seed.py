import sys

sys.path.append('./')
from fastapi import HTTPException, status
from db.Connexion import SessionLocal

from models.Models import Permission, User
# sys.path.append('.')
from passlib.handlers.sha2_crypt import sha512_crypt as crypto
from seed import create_permissions
from data import permission_data
from dotenv import load_dotenv
import os

load_dotenv()

user = User()
permissions = [
    {'name': "Acl_adm_read", 'description': "Read a vendor or an administrator", 'mode':'R', 'model_name': 'user'},
    {'name': "Acl_adm_create", 'description': "Create a vendor or an administrator", 'mode':'W', 'model_name': 'user'},
    {'name': "Acl_adm_delete", 'description': "Delete a vendor or an administrator", 'mode':'D', 'model_name': 'user'},
]

def create_admin():
    try:
        db = SessionLocal()

        # make sure the permissions are created
        create_permissions(permission_data, db)

        # create the admin user
        user = User()
        user.username = os.getenv('ADMIN_USERNAME')
        user.email = os.getenv('ADMIN_EMAIL')
        user.password = crypto.hash(os.getenv('ADMIN_PASSWORD'))
        user.roles = "Role_admin"
        user.status = "A"
        user.company_id = -2
        user.default_language = "en"
        permissions = db.query(Permission).filter(Permission.model_name == "user").all()
        permissions = [p for p in permissions if p.name.startswith('Acl_admin')]
        if not len(permissions):
            print("No permissions found in the permission table")
            exit()
        for p in permissions:
            user.permissions.append(p)
        # check if the user already exists before adding it
        if db.query(User).filter(User.username == user.username).first():
            print("User already exists")
        else:
            db.add(user)
            db.commit()
            print("Admin user created")
    except Exception as e:
        print(str(e))
    finally:
        db.close()


def main():
    create_admin()

if __name__ == '__main__':
    main()