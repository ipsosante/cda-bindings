from dataclasses import dataclass, field
from cda.org.hl7.v3.binary_data_encoding import BinaryDataEncoding
from cda.org.hl7.v3.ed import ED

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ST(ED):
    """
    The character string data type stands for text data, primarily intended for
    machine processing (e.g., sorting, querying, indexing, etc.) Used for
    names, symbols, and formal expressions.
    """
    representation: BinaryDataEncoding = field(
        init=False,
        default=BinaryDataEncoding.TXT,
        metadata={
            "type": "Attribute",
        }
    )
    media_type: str = field(
        init=False,
        default="text/plain",
        metadata={
            "name": "mediaType",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
