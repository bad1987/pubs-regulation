import asyncio
import datetime
from unittest import TestCase
import unittest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
import sys
sys.path.append("../..")

from schemas.ProduitConsession import ProduitConsessionSchema

from models.produitConcession import ProduitConcession
from models.dispositifs import DispositifPub
from models.typeDispositif import TypeDispositif
from models.emplacementAffichage import EmplacementAffichage
from models.tiers import Tiers, TypeTiers

from main import app
from db.Connexion import SessionLocal

class TestProduitConcession(TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.db = SessionLocal()
        # create test data