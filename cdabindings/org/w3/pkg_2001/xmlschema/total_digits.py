from dataclasses import dataclass
from cdabindings.org.w3.pkg_2001.xmlschema.num_facet import NumFacet

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class TotalDigits(NumFacet):
    class Meta:
        name = "totalDigits"
        namespace = "http://www.w3.org/2001/XMLSchema"
