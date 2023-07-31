from pydantic import BaseModel
from schemas.CampagneProduitSchema import CampagneProduitSchema
from schemas.DocEnteteSchema import DocEnteteSchema

class DocLigneSchema(BaseModel):
    IDDocLigne: int
    NumLigne: int
    MontantTTCLigne: float
    SurfaceOccupeFact: float
    MontantTaxeLigne: float
    MontantHTLigne: int
    IDDocEntete: int
    IDCampagneProduit: int
    doc_entete: DocEnteteSchema
    campagne_produit: CampagneProduitSchema

    class Config:
        orm_mode = True
        from_attributes = True

class DocLigneCreateSchema(BaseModel):
    NumLigne: int
    MontantTTCLigne: float
    SurfaceOccupeFact: float
    MontantTaxeLigne: float
    MontantHTLigne: int
    IDDocEntete: int
    IDCampagneProduit: int

class DocLigneUpdateSchema(BaseModel):
    IDDocLigne: int
    NumLigne: int
    MontantTTCLigne: float
    SurfaceOccupeFact: float
    MontantTaxeLigne: float
    MontantHTLigne: int
    IDDocEntete: int
    IDCampagneProduit: int