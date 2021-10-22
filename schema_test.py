from pydantic import BaseModel, Field
from typing import List, Optional


class PropertyUnit(BaseModel):
    """
    Representerer en bruksenhet.
    """
    property_unit_id: Optional[str] = Field(None, title='ID', description='ID for bruksenhet', unit='', example="1")
    coord_x: float = Field(..., title='Øst-koordinat', description='Øst-koordinat (UTM-32)', example=569616.247)
    coord_y: float = Field(..., title='Nord-koordinat', description='Nord-koordinat (UTM-32)', example=7034315.469)
    bygningstypekode: Optional[str] = Field(None, title='Bygningstypekode', description='Bygningstypekoden', example=111)
    tattibrukar: Optional[float] = Field(None, title='År tatt i bruk', description='Året bygningen ble tatt i bruk', unit='år', example="null")
    eiendomareal: Optional[float] = Field(None, title='Eiendomsareal', description='Eiendommens landareal', unit='m^2', example=600)
    bruksarealbruksenhet: Optional[float] = Field(None, title='Bruksareal bruksenhet', description='Det brukbare arealet i bruksenheten', unit='m^2', example=150)
    prom: Optional[float] = Field(None, title='Primærrom', description='Primærromsareal', unit='m^2', example="null")


class Property(BaseModel):
    """
    Denne klassen representerer en eiendom. Dersom det 2, 3 eller 4 bruksenheter på eiendommen og `override_property_unit_consolidation`
    er `False`, blir bruksenheter slått sammen. PROM og bruksarealbruksenhet summeres. For øvrige felter brukes verdi for første bruksenhet
    i listen. Dersom det er ulike verdier på bygningstypekode eller tattibrukar, settes flagget `est_unreliable`.
    """
    property_id: Optional[str] = Field(None, title='ID', description='ID for eiendom', example='5001-1-0-0-0')
    property_units: List[PropertyUnit] = Field(..., title='Bruksenheter', description='Liste over alle bruksenheter')
    