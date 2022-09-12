from dataclasses import dataclass
from cdabindings.org.w3.pkg_2001.xmlschema.element_1 import RealGroup

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class NamedGroup(RealGroup):
    class Meta:
        name = "namedGroup"
