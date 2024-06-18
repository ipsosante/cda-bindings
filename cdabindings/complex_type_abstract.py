from dataclasses import dataclass, field
from typing import Any, Optional, Union
from xml.etree.ElementTree import QName

from cdabindings.all_max_occurs import AllMaxOccurs
from cdabindings.all_min_occurs import AllMinOccurs
from cdabindings.all_nni_value import AllNniValue
from cdabindings.annotated import Annotated
from cdabindings.any import AnyType
from cdabindings.any_attribute import AnyAttribute
from cdabindings.attribute_2 import Attribute2
from cdabindings.attribute_group_abstract import AttributeGroupRef
from cdabindings.block_set import BlockSet
from cdabindings.derivation_set import DerivationSet
from cdabindings.enumeration import Enumeration
from cdabindings.form_choice import FormChoice
from cdabindings.fraction_digits import FractionDigits
from cdabindings.key_1 import Key1
from cdabindings.keyref import Keyref
from cdabindings.length import Length
from cdabindings.max_exclusive import MaxExclusive
from cdabindings.max_inclusive import MaxInclusive
from cdabindings.max_length import MaxLength
from cdabindings.min_exclusive import MinExclusive
from cdabindings.min_inclusive import MinInclusive
from cdabindings.min_length import MinLength
from cdabindings.pattern import Pattern
from cdabindings.simple_type_abstract import LocalSimpleType
from cdabindings.total_digits import TotalDigits
from cdabindings.unique import Unique
from cdabindings.white_space import WhiteSpace

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class ComplexTypeAbstract(Annotated):
    """
    :ivar simple_content:
    :ivar complex_content:
    :ivar group:
    :ivar all:
    :ivar choice:
    :ivar sequence:
    :ivar attribute:
    :ivar attribute_group:
    :ivar any_attribute:
    :ivar name: Will be restricted to required or forbidden
    :ivar mixed: Not allowed if simpleContent child is chosen. May be
        overriden by setting on complexContent child.
    :ivar abstract:
    :ivar final:
    :ivar block:
    """

    class Meta:
        name = "complexType"

    simple_content: Optional["SimpleContent"] = field(
        default=None,
        metadata={
            "name": "simpleContent",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    complex_content: Optional["ComplexContent"] = field(
        default=None,
        metadata={
            "name": "complexContent",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    group: Optional["GroupRef"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    all: Optional["All"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    choice: Optional["Choice"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    sequence: Optional["Sequence1"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    attribute: list[Attribute2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    attribute_group: list[AttributeGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    any_attribute: Optional[AnyAttribute] = field(
        default=None,
        metadata={
            "name": "anyAttribute",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mixed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    abstract: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    final: Optional[DerivationSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    block: Optional[DerivationSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LocalComplexType(ComplexTypeAbstract):
    class Meta:
        name = "localComplexType"

    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    name: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    abstract: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    final: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    block: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Element1(Annotated):
    """The element element can be used either at the top level to define an
    element-type binding globally, or within a content model to either reference a
    globally-defined element or type or declare an element-type binding locally.

    The ref form is not allowed at the top level.
    """

    class Meta:
        name = "element"

    simple_type: Optional[LocalSimpleType] = field(
        default=None,
        metadata={
            "name": "simpleType",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    complex_type: Optional[LocalComplexType] = field(
        default=None,
        metadata={
            "name": "complexType",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    unique: list[Unique] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    key: list[Key1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    keyref: list[Keyref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Optional[QName] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    substitution_group: Optional[QName] = field(
        default=None,
        metadata={
            "name": "substitutionGroup",
            "type": "Attribute",
        },
    )
    min_occurs: int = field(
        default=1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        },
    )
    max_occurs: Union[int, AllNniValue] = field(
        default=1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
        },
    )
    default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fixed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nillable: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    abstract: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    final: Optional[DerivationSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    block: Optional[BlockSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    form: Optional[FormChoice] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LocalElement(Element1):
    class Meta:
        name = "localElement"

    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    substitution_group: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    final: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    abstract: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class GroupAbstract(Annotated):
    """
    Group type for explicit groups, named top-level groups and group references.
    """

    class Meta:
        name = "group"

    element: list[LocalElement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    group: list["GroupRef"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    all: list["All"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    choice: list["Choice"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    sequence: list["Sequence1"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    any: list[AnyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    min_occurs: int = field(
        default=1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        },
    )
    max_occurs: Union[int, AllNniValue] = field(
        default=1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
        },
    )


@dataclass
class ExplicitGroup(GroupAbstract):
    """
    Group type for the three kinds of group.
    """

    class Meta:
        name = "explicitGroup"

    all: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    name: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class RealGroup(GroupAbstract):
    class Meta:
        name = "realGroup"

    element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    group: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class All(ExplicitGroup):
    """
    Only elements allowed inside.
    """

    class Meta:
        name = "all"
        namespace = "http://www.w3.org/2001/XMLSchema"

    all: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    group: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    choice: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    sequence: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    min_occurs: AllMinOccurs = field(
        default=AllMinOccurs.VALUE_1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        },
    )
    max_occurs: AllMaxOccurs = field(
        default=AllMaxOccurs.VALUE_1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
        },
    )


@dataclass
class Choice(ExplicitGroup):
    class Meta:
        name = "choice"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class GroupRef(RealGroup):
    class Meta:
        name = "groupRef"

    element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    group: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    all: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    choice: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    sequence: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    ref: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    name: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class Sequence1(ExplicitGroup):
    class Meta:
        name = "sequence"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class ExtensionType(Annotated):
    class Meta:
        name = "extensionType"

    group: Optional[GroupRef] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    all: Optional[All] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    choice: Optional[Choice] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    sequence: Optional[Sequence1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    attribute: list[Attribute2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    attribute_group: list[AttributeGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    any_attribute: Optional[AnyAttribute] = field(
        default=None,
        metadata={
            "name": "anyAttribute",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    base: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class RestrictionType(Annotated):
    class Meta:
        name = "restrictionType"

    group: Optional[GroupRef] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    all: Optional[All] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    choice: Optional[Choice] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    sequence: Optional[Sequence1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    simple_type: Optional[LocalSimpleType] = field(
        default=None,
        metadata={
            "name": "simpleType",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    min_exclusive: list[MinExclusive] = field(
        default_factory=list,
        metadata={
            "name": "minExclusive",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    min_inclusive: list[MinInclusive] = field(
        default_factory=list,
        metadata={
            "name": "minInclusive",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    max_exclusive: list[MaxExclusive] = field(
        default_factory=list,
        metadata={
            "name": "maxExclusive",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    max_inclusive: list[MaxInclusive] = field(
        default_factory=list,
        metadata={
            "name": "maxInclusive",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    total_digits: list[TotalDigits] = field(
        default_factory=list,
        metadata={
            "name": "totalDigits",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    fraction_digits: list[FractionDigits] = field(
        default_factory=list,
        metadata={
            "name": "fractionDigits",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    length: list[Length] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    min_length: list[MinLength] = field(
        default_factory=list,
        metadata={
            "name": "minLength",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    max_length: list[MaxLength] = field(
        default_factory=list,
        metadata={
            "name": "maxLength",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    enumeration: list[Enumeration] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    white_space: list[WhiteSpace] = field(
        default_factory=list,
        metadata={
            "name": "whiteSpace",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    pattern: list[Pattern] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    attribute: list[Attribute2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    attribute_group: list[AttributeGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    any_attribute: Optional[AnyAttribute] = field(
        default=None,
        metadata={
            "name": "anyAttribute",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    base: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ComplexRestrictionType(RestrictionType):
    class Meta:
        name = "complexRestrictionType"

    simple_type: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    min_exclusive: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    min_inclusive: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    max_exclusive: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    max_inclusive: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    total_digits: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    fraction_digits: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    length: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    min_length: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    max_length: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    enumeration: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    white_space: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    pattern: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class SimpleExtensionType(ExtensionType):
    class Meta:
        name = "simpleExtensionType"

    group: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    all: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    choice: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    sequence: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class SimpleRestrictionType(RestrictionType):
    class Meta:
        name = "simpleRestrictionType"

    group: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    all: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    choice: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    sequence: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    any_element: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class ComplexContent(Annotated):
    """
    :ivar restriction:
    :ivar extension:
    :ivar mixed: Overrides any setting on complexType parent.
    """

    class Meta:
        name = "complexContent"
        namespace = "http://www.w3.org/2001/XMLSchema"

    restriction: Optional[ComplexRestrictionType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    mixed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SimpleContent(Annotated):
    class Meta:
        name = "simpleContent"
        namespace = "http://www.w3.org/2001/XMLSchema"

    restriction: Optional[SimpleRestrictionType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    extension: Optional[SimpleExtensionType] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
