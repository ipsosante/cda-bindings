from dataclasses import dataclass

from cdabindings.top_level_simple_type import TopLevelSimpleType

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class SimpleType(TopLevelSimpleType):
    class Meta:
        name = "simpleType"
        namespace = "http://www.w3.org/2001/XMLSchema"
