import asyncio
import datetime
from unittest import TestCase
import unittest
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
import sys
sys.path.append("../..")

from schemas.PiecesSchema import PiecesSchema

from models.tiers import Tiers, TypeTiers
from models.docentete import DocEntete
from models.reglements import Reglement
from models.pieces import Piece, TypePiece

from main import app
from db.Connexion import SessionLocal

class TestPieces(TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.db = SessionLocal()
        # creata type tiers
        self.type_tiers = TypeTiers(LibelleTypeTiers="test TypeTiers")
        self.db.add(self.type_tiers)
        # creata tiers
        self.tiers = Tiers(CodeTiers="Test Code", LibelleTiers="Test LibelleTiers", AdresseTiers="Test AdresseTiers", TelephoneTiers=691796631, IDTypeTiers=self.type_tiers.IDTypeTiers, NumCont="Test NumCont",EmailTiers="Test EmailTiers", Logo="Test Logo",SigleTiers="TS")
        self.tiers.type_tiers = self.type_tiers
        self.db.add(self.tiers)
        # create doc entete
        self.doc_entete = DocEntete(TypeDocEntete=1, NumDocEntete="Test Num", DateDocEntete=datetime.datetime.utcnow(), MontantHTDoc=1000, MontantTaxeDoc=0, MontantTTCDoc=0, StatutDoc="AV", PenalitesDoc=0, IDTiers=self.tiers.IDTiers)
        self.doc_entete.tiers = self.tiers
        self.db.add(self.doc_entete)
        # create reglement
        self.reglement = Reglement(NumReglt="Test Num", DateReglt=datetime.datetime.utcnow(), MontantRegle=1000, SoldeRglt=0, StatutRglt="AC", ModeRglt="Test Mode", IDDocEntete=self.doc_entete.IDDocEntete)
        self.reglement.doc_entete = self.doc_entete
        self.db.add(self.reglement)
        # create tyes pieces
        self.type_pieces = TypePiece(LibelleTypePiece="test TypePieces")
        self.db.add(self.type_pieces)
        # create pieces
        self.pieces = Piece(NumPiece="Test Num", DateEmmission=datetime.datetime.utcnow(), IDReglement=self.reglement.IDReglement, IDTypePiece=self.type_pieces.IDTypePiece)
        self.pieces.reglement = self.reglement
        self.pieces.type_piece = self.type_pieces
        self.db.add(self.pieces)
        self.db.commit()
        self.db.refresh(self.type_tiers)
        self.db.refresh(self.tiers)
        self.db.refresh(self.doc_entete)
        self.db.refresh(self.reglement)
        self.db.refresh(self.pieces)
        self.db.refresh(self.type_pieces)
    
    def tearDown(self):
        # remove test data
        TypeTiers.delete(self.db, self.type_tiers.IDTypeTiers)
        # Tiers.delete(self.db, self.tiers.IDTiers)
        # DocEntete.delete(self.db, self.doc_entete.IDDocEntete)
        # Reglement.delete(self.db, self.reglement.IDReglement)
        TypePiece.delete(self.db, self.type_pieces.IDTypePiece)
        # Piece.delete(self.db, self.pieces.IDPiece)
        self.db.commit()
        self.db.close()
    
    async def test_get_by_NumPiece(self):
        # Test case 1: valid NumPiece
        num_piece = self.pieces.NumPiece
        response = self.client.get(f"/pieces/numPiece", params={"NumPiece": num_piece})
        self.assertEqual(response.status_code, 200)
        expected_result = PiecesSchema.model_validate(self.pieces).model_dump()
        expected_result["DateReglt"] = expected_result["DateReglt"].isoformat()
        self.assertEqual(response.json(), expected_result)

        # Test case 2: invalid NumPiece
        num_piece = "Num Test"
        response = self.client.get(f"/pieces/numPiece", params={"NumPiece": num_piece})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Piece not found"})

    async def test_get_by_id(self):
        # Test case 1: valid ID
        id_piece = self.pieces.IDPiece
        response = self.client.get(f"/pieces/{id_piece}")
        self.assertEqual(response.status_code, 200)
        expected_result = PiecesSchema.model_validate(self.pieces).model_dump()
        expected_result["DateReglt"] = expected_result["DateReglt"].isoformat()
        self.assertEqual(response.json(), expected_result)

        # Test case 2: invalid ID
        id_piece = 100000
        response = self.client.get(f"/pieces/{id_piece}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Piece not found"})

    async def test_get_all(self):
        response = self.client.get("/pieces")
        self.assertEqual(response.status_code, 200)
        expected_result = [PiecesSchema.model_validate(self.pieces).model_dump()]
        self.assertEqual(response.json(), expected_result)

    async def test_create_piece(self):
        post_data = {
            "NumPiece": "Test C Num",
            "DateEmmission": datetime.datetime.utcnow(),
            "IDReglement": self.reglement.IDReglement,
            "IDTypePiece": self.type_pieces.IDTypePiece
        }
        response = self.client.post("/pieces", json=post_data)
        self.assertEqual(response.status_code, 201)
        expected_result = self.client.get("/pieces/numPiece", params={"NumPiece": post_data["NumPiece"]})
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())

        # clean up through delete endpoint
        response = self.client.delete(f"/pieces/{expected_result.json()['IDPiece']}")
        self.assertEqual(response.status_code, 204)

    async def test_update_piece(self):
        post_data = {
            "IDPiece": self.pieces.IDPiece,
            "NumPiece": "Test U Num",
            "DateEmmission": datetime.datetime.utcnow(),
            "IDReglement": self.reglement.IDReglement,
            "IDTypePiece": self.type_pieces.IDTypePiece
        }
        response = self.client.put(f"/pieces/{self.pieces.IDPiece}", json=post_data)
        self.assertEqual(response.status_code, 201)
        expected_result = self.client.get("/pieces/numPiece", params={"NumPiece": post_data["NumPiece"]})
        self.assertEqual(expected_result.status_code, 200)
        self.assertEqual(response.json(), expected_result.json())

if __name__ == "__main__":
    unittest.main()