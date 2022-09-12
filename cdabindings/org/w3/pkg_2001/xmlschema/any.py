from dataclasses import dataclass, field
from typing import Union
from cdabindings.org.w3.pkg_2001.xmlschema.all_nni_value import AllNniValue
from cdabindings.org.w3.pkg_2001.xmlschema.wildcard import Wildcard

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Any(Wildcard):
    class Meta:
        name = "any"
        namespace = "http://www.w3.org/2001/XMLSchema"

    min_occurs: int = field(
        default=1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: Union[int, AllNniValue] = field(
        default=1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
        }
    )
