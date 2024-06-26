from dataclasses import dataclass, field

from cdabindings.any_abstract import AnyAbstract
from cdabindings.binary_data_encoding import BinaryDataEncoding

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Bin(AnyAbstract):
    """Binary data is a raw block of bits.

    Binary data is a protected type that MUST not be used outside the
    data type specification.

    :ivar representation: Specifies the representation of the binary
        data that is the content of the binary data value.
    :ivar content:
    """

    class Meta:
        name = "BIN"

    representation: BinaryDataEncoding = field(
        default=BinaryDataEncoding.TXT,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
