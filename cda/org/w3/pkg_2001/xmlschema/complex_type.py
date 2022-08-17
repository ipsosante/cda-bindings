from dataclasses import dataclass
from cda.org.w3.pkg_2001.xmlschema.top_level_complex_type import TopLevelComplexType

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class ComplexType(TopLevelComplexType):
    class Meta:
        name = "complexType"
        namespace = "http://www.w3.org/2001/XMLSchema"
