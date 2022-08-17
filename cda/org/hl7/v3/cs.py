from dataclasses import dataclass
from cda.org.hl7.v3.cr import CV

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CS(CV):
    """Coded data, consists of a code, display name, code system, and original
    text.

    Used when a single code value must be sent.
    """
