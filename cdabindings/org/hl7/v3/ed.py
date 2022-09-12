from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.hl7.v3.bin import Bin
from cdabindings.org.hl7.v3.compression_algorithm import CompressionAlgorithm
from cdabindings.org.hl7.v3.integrity_check_algorithm import IntegrityCheckAlgorithm

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ED(Bin):
    """Data that is primarily intended for human interpretation or for further
    machine processing is outside the scope of HL7.

    This includes unformatted or formatted written language, multimedia
    data, or structured information as defined by a different standard
    (e.g., XML-signatures.)  Instead of the data itself, an ED may
    contain only a reference (see TEL.) Note that the ST data type is a
    specialization of when the  is text/plain.

    :ivar media_type: Identifies the type of the encapsulated data and
        identifies a method to interpret or render the data.
    :ivar language: For character based information the language
        property specifies the human language of the text.
    :ivar compression: Indicates whether the raw byte data is
        compressed, and what compression algorithm was used.
    :ivar integrity_check: The integrity check is a short binary value
        representing a cryptographically strong checksum that is
        calculated over the binary data. The purpose of this property,
        when communicated with a reference is for anyone to validate
        later whether the reference still resolved to the same data that
        the reference resolved to when the encapsulated data value with
        reference was created.
    :ivar integrity_check_algorithm: Specifies the algorithm used to
        compute the integrityCheck value.
    """
    media_type: str = field(
        default="text/plain",
        metadata={
            "name": "mediaType",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    compression: Optional[CompressionAlgorithm] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    integrity_check: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "integrityCheck",
            "type": "Attribute",
            "format": "base64",
        }
    )
    integrity_check_algorithm: IntegrityCheckAlgorithm = field(
        default=IntegrityCheckAlgorithm.SHA_1,
        metadata={
            "name": "integrityCheckAlgorithm",
            "type": "Attribute",
        }
    )
