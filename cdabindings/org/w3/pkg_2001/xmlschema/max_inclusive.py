from dataclasses import dataclass
from cdabindings.org.w3.pkg_2001.xmlschema.facet import Facet

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class MaxInclusive(Facet):
    class Meta:
        name = "maxInclusive"
        namespace = "http://www.w3.org/2001/XMLSchema"