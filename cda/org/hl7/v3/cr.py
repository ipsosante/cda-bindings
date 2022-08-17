from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.hl7.v3.any import Any
from cda.org.hl7.v3.ed import ED

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Cr(Any):
    """A concept qualifier code with optionally named role.

    Both qualifier role and value codes must be defined by the coding
    system.  For example, if SNOMED RT defines a concept "leg", a role
    relation "has-laterality", and another concept "left", the concept
    role relation allows to add the qualifier "has-laterality: left" to
    a primary code "leg" to construct the meaning "left leg".

    :ivar name: Specifies the manner in which the concept role value
        contributes to the meaning of a code phrase.  For example, if
        SNOMED RT defines a concept "leg", a role relation "has-
        laterality", and another concept "left", the concept role
        relation allows to add the qualifier "has-laterality: left" to a
        primary code "leg" to construct the meaning "left leg".  In this
        example "has-laterality" is .
    :ivar value: The concept that modifies the primary code of a code
        phrase through the role relation.  For example, if SNOMED RT
        defines a concept "leg", a role relation "has-laterality", and
        another concept "left", the concept role relation allows adding
        the qualifier "has-laterality: left" to a primary code "leg" to
        construct the meaning "left leg".  In this example "left" is .
    :ivar inverted: Indicates if the sense of the role name is inverted.
        This can be used in cases where the underlying code system
        defines inversion but does not provide reciprocal pairs of role
        names. By default, inverted is false.
    """
    class Meta:
        name = "CR"

    name: Optional["CV"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    value: Optional["CD"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    inverted: str = field(
        default="false",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CD(Any):
    """A concept descriptor represents any kind of concept usually by giving a
    code defined in a code system.

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
    :ivar qualifier: Specifies additional codes that increase the
        specificity of the primary code.
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
        }
    )
    qualifier: List[Cr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    translation: List["CD"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    code_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystem",
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    code_system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    code_system_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSystemVersion",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    value_set: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSet",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    value_set_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "valueSetVersion",
            "type": "Attribute",
            "namespace": "urn:hl7-org:sdtc",
            "min_length": 1,
        }
    )


@dataclass
class CE(CD):
    """Coded data, consists of a coded value (CV) and, optionally, coded
    value(s) from other coding systems that identify the same concept.

    Used when alternative codes may exist.
    """


@dataclass
class CV(CE):
    """Coded data, consists of a code, display name, code system, and original
    text.

    Used when a single code value must be sent.
    """
