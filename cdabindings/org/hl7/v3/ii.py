from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.hl7.v3.any import Any

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class II(Any):
    """An identifier that uniquely identifies a thing or object.

    Examples are object identifier for HL7 RIM objects, medical record
    number, order id, service catalog item id, Vehicle Identification
    Number (VIN), etc. Instance identifiers are defined based on ISO
    object identifiers.

    :ivar root: A unique identifier that guarantees the global
        uniqueness of the instance identifier. The root alone may be the
        entire instance identifier.
    :ivar extension: A character string as a unique identifier within
        the scope of the identifier root.
    :ivar assigning_authority_name: A human readable name or mnemonic
        for the assigning authority. This name may be provided solely
        for the convenience of unaided humans interpreting an  value and
        can have no computational meaning. Note: no automated processing
        must depend on the assigning authority name to be present in any
        form.
    :ivar displayable: Specifies if the identifier is intended for human
        display and data entry (displayable = true) as opposed to pure
        machine interoperation (displayable = false).
    """
    root: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    extension: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 1,
        }
    )
    assigning_authority_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigningAuthorityName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    displayable: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )
