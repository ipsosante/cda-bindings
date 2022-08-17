from dataclasses import dataclass
from cda.org.w3.pkg_2001.xmlschema.element_1 import ExplicitGroup

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class SimpleExplicitGroup(ExplicitGroup):
    class Meta:
        name = "simpleExplicitGroup"
