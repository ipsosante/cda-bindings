from dataclasses import dataclass

from cdabindings.num_facet import NumFacet

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class MaxLength(NumFacet):
    class Meta:
        name = "maxLength"
        namespace = "http://www.w3.org/2001/XMLSchema"
