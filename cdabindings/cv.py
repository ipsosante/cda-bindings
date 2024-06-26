from dataclasses import dataclass

from cdabindings.ce import CE

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CV(CE):
    """Coded data, consists of a code, display name, code system, and original
    text.

    Used when a single code value must be sent.
    """
