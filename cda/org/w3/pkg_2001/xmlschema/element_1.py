from dataclasses import dataclass, field
from typing import List, Optional, Union
from xml.etree.ElementTree import QName
from cda.org.w3.pkg_2001.xmlschema.all_max_occurs import AllMaxOccurs
from cda.org.w3.pkg_2001.xmlschema.all_min_occurs import AllMinOccurs
from cda.org.w3.pkg_2001.xmlschema.all_nni_value import AllNniValue
from cda.org.w3.pkg_2001.xmlschema.annotated import Annotated
from cda.org.w3.pkg_2001.xmlschema.any import Any
from cda.org.w3.pkg_2001.xmlschema.any_attribute import AnyAttribute
from cda.org.w3.pkg_2001.xmlschema.attribute import Attribute
from cda.org.w3.pkg_2001.xmlschema.attribute_group_1 import AttributeGroupRef
from cda.org.w3.pkg_2001.xmlschema.block_set import BlockSet
from cda.org.w3.pkg_2001.xmlschema.derivation_set import DerivationSet
from cda.org.w3.pkg_2001.xmlschema.enumeration import Enumeration
from cda.org.w3.pkg_2001.xmlschema.form_choice import FormChoice
from cda.org.w3.pkg_2001.xmlschema.fraction_digits import FractionDigits
from cda.org.w3.pkg_2001.xmlschema.key import Key
from cda.org.w3.pkg_2001.xmlschema.keyref import Keyref
from cda.org.w3.pkg_2001.xmlschema.length import Length
from cda.org.w3.pkg_2001.xmlschema.list_mod import LocalSimpleType
from cda.org.w3.pkg_2001.xmlschema.max_exclusive import MaxExclusive
from cda.org.w3.pkg_2001.xmlschema.max_inclusive import MaxInclusive
from cda.org.w3.pkg_2001.xmlschema.max_length import MaxLength
from cda.org.w3.pkg_2001.xmlschema.min_exclusive import MinExclusive
from cda.org.w3.pkg_2001.xmlschema.min_inclusive import MinInclusive
from cda.org.w3.pkg_2001.xmlschema.min_length import MinLength
from cda.org.w3.pkg_2001.xmlschema.pattern import Pattern
from cda.org.w3.pkg_2001.xmlschema.total_digits import TotalDigits
from cda.org.w3.pkg_2001.xmlschema.unique import Unique
from cda.org.w3.pkg_2001.xmlschema.white_space import WhiteSpace

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Element1(Annotated):
    """The element element can be used either at the top level to define an
    element-type binding globally, or within a content model to either
    reference a globally-defined element or type or declare an element-type
    binding locally.

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
        }
    )
    complex_type: Optional["LocalComplexType"] = field(
        default=None,
        metadata={
            "name": "complexType",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    unique: List[Unique] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    key: List[Key] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    keyref: List[Keyref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ref: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    substitution_group: Optional[QName] = field(
        default=None,
        metadata={
            "name": "substitutionGroup",
            "type": "Attribute",
        }
    )
    min_occurs: int = field(
        default=1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: Union[int, AllNniValue] = field(
        default=1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
        }
    )
    default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    fixed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nillable: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    abstract: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    final: Optional[DerivationSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    block: Optional[BlockSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    form: Optional[FormChoice] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ExtensionType(Annotated):
    class Meta:
        name = "extensionType"

    group: Optional["GroupRef"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    all: Optional["All"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    choice: Optional["Choice"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    sequence: Optional["Sequence"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    attribute: List[Attribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
            "sequential": True,
        }
    )
    attribute_group: List[AttributeGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
            "sequential": True,
        }
    )
    any_attribute: Optional[AnyAttribute] = field(
        default=None,
        metadata={
            "name": "anyAttribute",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    base: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RestrictionType(Annotated):
    class Meta:
        name = "restrictionType"

    group: Optional["GroupRef"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    all: Optional["All"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    choice: Optional["Choice"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    sequence: Optional["Sequence"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    simple_type: Optional[LocalSimpleType] = field(
        default=None,
        metadata={
            "name": "simpleType",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    min_exclusive: List[MinExclusive] = field(
        default_factory=list,
        metadata={
            "name": "minExclusive",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    min_inclusive: List[MinInclusive] = field(
        default_factory=list,
        metadata={
            "name": "minInclusive",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    max_exclusive: List[MaxExclusive] = field(
        default_factory=list,
        metadata={
            "name": "maxExclusive",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    max_inclusive: List[MaxInclusive] = field(
        default_factory=list,
        metadata={
            "name": "maxInclusive",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    total_digits: List[TotalDigits] = field(
        default_factory=list,
        metadata={
            "name": "totalDigits",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    fraction_digits: List[FractionDigits] = field(
        default_factory=list,
        metadata={
            "name": "fractionDigits",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    length: List[Length] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    min_length: List[MinLength] = field(
        default_factory=list,
        metadata={
            "name": "minLength",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    max_length: List[MaxLength] = field(
        default_factory=list,
        metadata={
            "name": "maxLength",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    enumeration: List[Enumeration] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    white_space: List[WhiteSpace] = field(
        default_factory=list,
        metadata={
            "name": "whiteSpace",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    pattern: List[Pattern] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    attribute: List[Attribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
            "sequential": True,
        }
    )
    attribute_group: List[AttributeGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
            "sequential": True,
        }
    )
    any_attribute: Optional[AnyAttribute] = field(
        default=None,
        metadata={
            "name": "anyAttribute",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    base: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ComplexRestrictionType(RestrictionType):
    class Meta:
        name = "complexRestrictionType"


@dataclass
class LocalElement(Element1):
    class Meta:
        name = "localElement"


@dataclass
class SimpleExtensionType(ExtensionType):
    class Meta:
        name = "simpleExtensionType"


@dataclass
class SimpleRestrictionType(RestrictionType):
    class Meta:
        name = "simpleRestrictionType"


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
        }
    )
    extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mixed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Group1(Annotated):
    """
    group type for explicit groups, named top-level groups and group
    references.
    """
    class Meta:
        name = "group"

    element: List[LocalElement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    group: List["GroupRef"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    all: List["All"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    choice: List["Choice"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    sequence: List["Sequence"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    any: List[Any] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ref: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    min_occurs: int = field(
        default=1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: Union[int, AllNniValue] = field(
        default=1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
        }
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
        }
    )
    extension: Optional[SimpleExtensionType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class ExplicitGroup(Group1):
    """
    group type for the three kinds of group.
    """
    class Meta:
        name = "explicitGroup"


@dataclass
class RealGroup(Group1):
    class Meta:
        name = "realGroup"


@dataclass
class All(ExplicitGroup):
    """
    Only elements allowed inside.
    """
    class Meta:
        name = "all"
        namespace = "http://www.w3.org/2001/XMLSchema"

    min_occurs: AllMinOccurs = field(
        default=AllMinOccurs.VALUE_1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        }
    )
    max_occurs: AllMaxOccurs = field(
        default=AllMaxOccurs.VALUE_1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
        }
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


@dataclass
class Sequence(ExplicitGroup):
    class Meta:
        name = "sequence"
        namespace = "http://www.w3.org/2001/XMLSchema"


@dataclass
class ComplexType1(Annotated):
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

    simple_content: Optional[SimpleContent] = field(
        default=None,
        metadata={
            "name": "simpleContent",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    complex_content: Optional[ComplexContent] = field(
        default=None,
        metadata={
            "name": "complexContent",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    group: Optional[GroupRef] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    all: Optional[All] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    choice: Optional[Choice] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    sequence: Optional[Sequence] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    attribute: List[Attribute] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
            "sequential": True,
        }
    )
    attribute_group: List[AttributeGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "attributeGroup",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
            "sequential": True,
        }
    )
    any_attribute: Optional[AnyAttribute] = field(
        default=None,
        metadata={
            "name": "anyAttribute",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mixed: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    abstract: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    final: Optional[DerivationSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    block: Optional[DerivationSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class LocalComplexType(ComplexType1):
    class Meta:
        name = "localComplexType"
