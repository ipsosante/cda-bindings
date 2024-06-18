from dataclasses import dataclass, field
from typing import Any

from cdabindings.binary_data_encoding import BinaryDataEncoding
from cdabindings.compression_algorithm import CompressionAlgorithm
from cdabindings.ed import ED
from cdabindings.integrity_check_algorithm import IntegrityCheckAlgorithm

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ST(ED):
    """
    The character string data type stands for text data, primarily intended for
    machine processing (e.g., sorting, querying, indexing, etc.) Used for names,
    symbols, and formal expressions.
    """

    representation: BinaryDataEncoding = field(
        init=False,
        default=BinaryDataEncoding.TXT,
        metadata={
            "type": "Attribute",
        },
    )
    media_type: str = field(
        init=False,
        default="text/plain",
        metadata={
            "name": "mediaType",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        },
    )
    compression: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    integrity_check: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    integrity_check_algorithm: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
