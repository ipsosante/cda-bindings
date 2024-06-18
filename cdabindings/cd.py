from dataclasses import dataclass, field
from typing import Optional

from cdabindings.any_abstract import AnyAbstract
from cdabindings.ed import ED

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CD(AnyAbstract):
    """A concept descriptor represents any kind of concept usually by giving a code
    defined in a code system.

    A concept descriptor can contain the original text or phrase that
    served as the basis of the coding and one or more translations into
    different coding systems. A concept descriptor can also contain
    qualifiers to describe, e.g., the concept of a "left foot" as a
    postcoordinated term built from the primary code "FOOT" and the
    qualifier "LEFT". In exceptional cases, the concept descriptor need
    not contain a code but only the original text describing that
    concept.

    :ivar original_text: The text or phrase used as the basis for the
        coding.
    :ivar translation: A set of other concept descriptors that translate
        this concept descriptor into other code systems.
    :ivar code: The plain code symbol defined by the code system. For
        example, "784.0" is the code symbol of the ICD-9 code "784.0"
        for headache.
    :ivar code_system: Specifies the code system that defines the code.
    :ivar code_system_name: A common name of the coding system.
    :ivar code_system_version: If applicable, a version descriptor
        defined specifically for the given code system.
    :ivar display_name: A name or title for the code, under which the
        sending system shows the code value to its users.
    :ivar value_set:
    :ivar value_set_version:
    """

    original_text: Optional[ED] = field(
        default=None,
        metadata={
            "name": "originalText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    translation: list["CD"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        },
    )
    code_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        },
    )
    code_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Attribute",
            "min_length": 1,
        },
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Attribute",
            "min_length": 1,
        },
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
            "min_length": 1,
        },
    )
    value_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSet",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        },
    )
    value_set_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSetVersion",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "min_length": 1,
        },
    )
