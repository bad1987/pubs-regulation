
from datetime import date, datetime

from pydantic import BaseModel

from schemas.DocEnteteSchema import DocEnteteSchema


class ReglementSchema(BaseModel):
    IDReglement: int
    NumReglt: str
    DateReglt: datetime
    MontantRegle: int
    SoldeRglt: float
    StatutRglt: str
    ModeRglt: str
    IDDocEntete: int
    doc_entete: DocEnteteSchema

    class Config:
        orm_mode = True
        from_attributes = True

class ReglementCreateSchema(BaseModel):
    NumReglt: str
    DateReglt: date
    MontantRegle: int
    SoldeRglt: float
    StatutRglt: str
    ModeRglt: str
    IDDocEntete: int

class ReglementUpdateSchema(BaseModel):
    IDReglement: int
    NumReglt: str
    DateReglt: date
    MontantRegle: int
    SoldeRglt: float
    StatutRglt: str
    ModeRglt: str
    IDDocEntete: int