from dataclasses import dataclass, field
from typing import Optional

from cdabindings.any_abstract import AnyAbstract

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Url(AnyAbstract):
    """A telecommunications address  specified according to
    Internet standard RFC 1738
    [http://www.ietf.org/rfc/rfc1738.txt]. The
    URL specifies the protocol and the contact point defined
    by that protocol for the resource.  Notable uses of the
    telecommunication address data type are for telephone and
    telefax numbers, e-mail addresses, Hypertext references,
    FTP references, etc."""

    class Meta:
        name = "URL"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
