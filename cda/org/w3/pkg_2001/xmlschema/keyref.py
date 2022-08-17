from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from cda.org.w3.pkg_2001.xmlschema.keybase import Keybase

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Keyref(Keybase):
    class Meta:
        name = "keyref"
        namespace = "http://www.w3.org/2001/XMLSchema"

    refer: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
