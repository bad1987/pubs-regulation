# this class defines a pydantic schema for the TypePanneau model

from typing import Optional, List
from pydantic import BaseModel


class TypePanneauSchema(BaseModel):
    IDTypePanneau: Optional[int]
    CodeTypePanneau: Optional[str]
    LibelleType: Optional[str]

    class Config:
        orm_mode = True
        from_attributes = True

class TypePanneauCreateSchema(BaseModel):
    CodeTypePanneau: Optional[str]
    LibelleType: Optional[str]