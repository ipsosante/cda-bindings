from dataclasses import dataclass, field
from typing import Any, Optional
from xml.etree.ElementTree import QName

from cdabindings.annotated import Annotated
from cdabindings.enumeration import Enumeration
from cdabindings.fraction_digits import FractionDigits
from cdabindings.length import Length
from cdabindings.max_exclusive import MaxExclusive
from cdabindings.max_inclusive import MaxInclusive
from cdabindings.max_length import MaxLength
from cdabindings.min_exclusive import MinExclusive
from cdabindings.min_inclusive import MinInclusive
from cdabindings.min_length import MinLength
from cdabindings.pattern import Pattern
from cdabindings.simple_derivation_set import SimpleDerivationSet
from cdabindings.total_digits import TotalDigits
from cdabindings.white_space import WhiteSpace

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class SimpleTypeAbstract(Annotated):
    """
    :ivar restriction:
    :ivar list_value:
    :ivar union:
    :ivar final:
    :ivar name: Can be restricted to required or forbidden
    """

    class Meta:
        name = "simpleType"

    restriction: Optional["Restriction"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    list_value: Optional["ListType"] = field(
        default=None,
        metadata={
            "name": "list",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    union: Optional["UnionType"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        },
    )
    final: Optional[SimpleDerivationSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LocalSimpleType(SimpleTypeAbstract):
    """
    :ivar any_element:
    :ivar name: Forbidden when nested
    :ivar final:
    """

    class Meta:
        name = "localSimpleType"

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
    final: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class ListType(Annotated):
    class Meta:
        name = "list"
        namespace = "http://www.w3.org/2001/XMLSchema"

    simple_type: Optional[LocalSimpleType] = field(
        default=None,
        metadata={
            "name": "simpleType",
            "type": "Element",
        },
    )
    item_type: Optional[QName] = field(
        default=None,
        metadata={
            "name": "itemType",
            "type": "Attribute",
        },
    )


@dataclass
class Restriction(Annotated):
    class Meta:
        name = "restriction"
        namespace = "http://www.w3.org/2001/XMLSchema"

    simple_type: Optional[LocalSimpleType] = field(
        default=None,
        metadata={
            "name": "simpleType",
            "type": "Element",
        },
    )
    min_exclusive: list[MinExclusive] = field(
        default_factory=list,
        metadata={
            "name": "minExclusive",
            "type": "Element",
        },
    )
    min_inclusive: list[MinInclusive] = field(
        default_factory=list,
        metadata={
            "name": "minInclusive",
            "type": "Element",
        },
    )
    max_exclusive: list[MaxExclusive] = field(
        default_factory=list,
        metadata={
            "name": "maxExclusive",
            "type": "Element",
        },
    )
    max_inclusive: list[MaxInclusive] = field(
        default_factory=list,
        metadata={
            "name": "maxInclusive",
            "type": "Element",
        },
    )
    total_digits: list[TotalDigits] = field(
        default_factory=list,
        metadata={
            "name": "totalDigits",
            "type": "Element",
        },
    )
    fraction_digits: list[FractionDigits] = field(
        default_factory=list,
        metadata={
            "name": "fractionDigits",
            "type": "Element",
        },
    )
    length: list[Length] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    min_length: list[MinLength] = field(
        default_factory=list,
        metadata={
            "name": "minLength",
            "type": "Element",
        },
    )
    max_length: list[MaxLength] = field(
        default_factory=list,
        metadata={
            "name": "maxLength",
            "type": "Element",
        },
    )
    enumeration: list[Enumeration] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    white_space: list[WhiteSpace] = field(
        default_factory=list,
        metadata={
            "name": "whiteSpace",
            "type": "Element",
        },
    )
    pattern: list[Pattern] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    base: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class UnionType(Annotated):
    class Meta:
        name = "union"
        namespace = "http://www.w3.org/2001/XMLSchema"

    simple_type: list[LocalSimpleType] = field(
        default_factory=list,
        metadata={
            "name": "simpleType",
            "type": "Element",
        },
    )
    member_types: list[QName] = field(
        default_factory=list,
        metadata={
            "name": "memberTypes",
            "type": "Attribute",
            "tokens": True,
        },
    )
