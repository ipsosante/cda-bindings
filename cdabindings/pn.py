from dataclasses import dataclass

from cdabindings.en import En

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class PN(En):
    """A name for a person.

    A sequence of name parts, such as given name or family name, prefix,
    suffix, etc. PN differs from EN because the qualifier type cannot
    include LS (Legal Status).
    """
