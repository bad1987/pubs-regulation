# this class defines a pydantic schema for the TypePanneau model

from typing import Optional
from pydantic import BaseModel


class TypePanneauSchema(BaseModel):
    IDTypePanneau: Optional[int]
    CodeTypePanneau: Optional[str]
    LibelleTypePanneau: Optional[str]
    panneaux: Optional[list]

    class Config:
        orm_mode = True

class TypePanneauCreateSchema(BaseModel):
    CodeTypePanneau: Optional[str]
    LibelleTypePanneau: Optional[str]