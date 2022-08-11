from enum import Enum
from strenum import StrEnum

class FlashCat(StrEnum):
    INFO="info"
    EXITO="success"
    FALLA="danger"
    ALERTA="warning"
