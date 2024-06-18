from dataclasses import dataclass, field
from typing import Optional

from cdabindings.any_abstract import AnyAbstract
from cdabindings.cd import CD
from cdabindings.cv import CV

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Cr(AnyAbstract):
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
        example "has-laterality" is the CR.name.
    :ivar value: The concept that modifies the primary code of a code
        phrase through the role relation.  For example, if SNOMED RT
        defines a concept "leg", a role relation "has-laterality", and
        another concept "left", the concept role relation allows adding
        the qualifier "has-laterality: left" to a primary code "leg" to
        construct the meaning "left leg".  In this example "left" is the
        CR.value.
    :ivar inverted: Indicates if the sense of the role name is inverted.
        This can be used in cases where the underlying code system
        defines inversion but does not provide reciprocal pairs of role
        names. By default, inverted is false.
    """

    class Meta:
        name = "CR"

    name: Optional[CV] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    value: Optional[CD] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    inverted: str = field(
        default="false",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )
