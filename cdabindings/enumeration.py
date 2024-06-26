from dataclasses import dataclass

from cdabindings.no_fixed_facet import NoFixedFacet

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Enumeration(NoFixedFacet):
    class Meta:
        name = "enumeration"
        namespace = "http://www.w3.org/2001/XMLSchema"
