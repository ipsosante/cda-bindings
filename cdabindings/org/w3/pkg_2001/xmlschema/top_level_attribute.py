from dataclasses import dataclass
from cdabindings.org.w3.pkg_2001.xmlschema.attribute_1 import Attribute1

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class TopLevelAttribute(Attribute1):
    class Meta:
        name = "topLevelAttribute"
