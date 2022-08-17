from dataclasses import dataclass
from cda.org.w3.pkg_2001.xmlschema.facet import Facet

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class MaxExclusive(Facet):
    class Meta:
        name = "maxExclusive"
        namespace = "http://www.w3.org/2001/XMLSchema"
