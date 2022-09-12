from dataclasses import dataclass
from cdabindings.org.w3.pkg_2001.xmlschema.list_mod import SimpleType1

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class TopLevelSimpleType(SimpleType1):
    class Meta:
        name = "topLevelSimpleType"
