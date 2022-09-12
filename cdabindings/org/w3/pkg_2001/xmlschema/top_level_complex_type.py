from dataclasses import dataclass
from cdabindings.org.w3.pkg_2001.xmlschema.element_1 import ComplexType1

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class TopLevelComplexType(ComplexType1):
    class Meta:
        name = "topLevelComplexType"
