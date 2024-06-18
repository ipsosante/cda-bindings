from dataclasses import dataclass

from cdabindings.num_facet import NumFacet

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class FractionDigits(NumFacet):
    class Meta:
        name = "fractionDigits"
        namespace = "http://www.w3.org/2001/XMLSchema"
