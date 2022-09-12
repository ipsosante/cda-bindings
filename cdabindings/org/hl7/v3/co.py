from dataclasses import dataclass
from cdabindings.org.hl7.v3.cr import CV

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Co(CV):
    """Coded data, where the domain from which the codeset comes is ordered.

    The Coded Ordinal data type adds semantics related to ordering so
    that models that make use of such domains may introduce model
    elements that involve statements about the order of the terms in a
    domain.
    """
    class Meta:
        name = "CO"
