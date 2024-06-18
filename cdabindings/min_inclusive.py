from dataclasses import dataclass

from cdabindings.facet import Facet

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class MinInclusive(Facet):
    class Meta:
        name = "minInclusive"
        namespace = "http://www.w3.org/2001/XMLSchema"
