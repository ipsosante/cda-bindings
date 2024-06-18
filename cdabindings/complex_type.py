from dataclasses import dataclass

from cdabindings.top_level_complex_type import TopLevelComplexType

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class ComplexType(TopLevelComplexType):
    class Meta:
        name = "complexType"
        namespace = "http://www.w3.org/2001/XMLSchema"
