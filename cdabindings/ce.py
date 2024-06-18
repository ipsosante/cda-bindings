from dataclasses import dataclass

from cdabindings.cd import CD

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CE(CD):
    """Coded data, consists of a coded value (CV) and, optionally, coded value(s)
    from other coding systems that identify the same concept.

    Used when alternative codes may exist.
    """
