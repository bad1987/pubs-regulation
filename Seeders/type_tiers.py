import sys
sys.path.append("..")
from models.tiers import TypeTiers
from db.Connexion import SessionLocal

db = SessionLocal()

list_type_tiers = [
    "Regisseur", "Regulateur", "Annonceur"
]
print("Creating Tiers")
for type in list_type_tiers:
    type_tiers = TypeTiers(LibelleTypeTiers=type)
    type_tiers = TypeTiers.create(db, type_tiers)
    print(f"{type_tiers.LibelleTypeTiers} created")
print("Done")