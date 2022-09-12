from dataclasses import dataclass
from cdabindings.org.w3.pkg_2001.xmlschema.no_fixed_facet import NoFixedFacet

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Pattern(NoFixedFacet):
    class Meta:
        name = "pattern"
        namespace = "http://www.w3.org/2001/XMLSchema"
