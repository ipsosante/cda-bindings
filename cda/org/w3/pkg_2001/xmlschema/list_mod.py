from dataclasses import dataclass, field
from typing import List, Optional
from xml.etree.ElementTree import QName
from cda.org.w3.pkg_2001.xmlschema.annotated import Annotated
from cda.org.w3.pkg_2001.xmlschema.enumeration import Enumeration
from cda.org.w3.pkg_2001.xmlschema.fraction_digits import FractionDigits
from cda.org.w3.pkg_2001.xmlschema.length import Length
from cda.org.w3.pkg_2001.xmlschema.max_exclusive import MaxExclusive
from cda.org.w3.pkg_2001.xmlschema.max_inclusive import MaxInclusive
from cda.org.w3.pkg_2001.xmlschema.max_length import MaxLength
from cda.org.w3.pkg_2001.xmlschema.min_exclusive import MinExclusive
from cda.org.w3.pkg_2001.xmlschema.min_inclusive import MinInclusive
from cda.org.w3.pkg_2001.xmlschema.min_length import MinLength
from cda.org.w3.pkg_2001.xmlschema.pattern import Pattern
from cda.org.w3.pkg_2001.xmlschema.simple_derivation_set import SimpleDerivationSet
from cda.org.w3.pkg_2001.xmlschema.total_digits import TotalDigits
from cda.org.w3.pkg_2001.xmlschema.white_space import WhiteSpace

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class ListType(Annotated):
    class Meta:
        name = "list"
        namespace = "http://www.w3.org/2001/XMLSchema"

    simple_type: Optional["LocalSimpleType"] = field(
        default=None,
        metadata={
            "name": "simpleType",
            "type": "Element",
        }
    )
    item_type: Optional[QName] = field(
        default=None,
        metadata={
            "name": "itemType",
            "type": "Attribute",
        }
    )


@dataclass
class Restriction(Annotated):
    class Meta:
        name = "restriction"
        namespace = "http://www.w3.org/2001/XMLSchema"

    simple_type: Optional["LocalSimpleType"] = field(
        default=None,
        metadata={
            "name": "simpleType",
            "type": "Element",
        }
    )
    min_exclusive: List[MinExclusive] = field(
        default_factory=list,
        metadata={
            "name": "minExclusive",
            "type": "Element",
        }
    )
    min_inclusive: List[MinInclusive] = field(
        default_factory=list,
        metadata={
            "name": "minInclusive",
            "type": "Element",
        }
    )
    max_exclusive: List[MaxExclusive] = field(
        default_factory=list,
        metadata={
            "name": "maxExclusive",
            "type": "Element",
        }
    )
    max_inclusive: List[MaxInclusive] = field(
        default_factory=list,
        metadata={
            "name": "maxInclusive",
            "type": "Element",
        }
    )
    total_digits: List[TotalDigits] = field(
        default_factory=list,
        metadata={
            "name": "totalDigits",
            "type": "Element",
        }
    )
    fraction_digits: List[FractionDigits] = field(
        default_factory=list,
        metadata={
            "name": "fractionDigits",
            "type": "Element",
        }
    )
    length: List[Length] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    min_length: List[MinLength] = field(
        default_factory=list,
        metadata={
            "name": "minLength",
            "type": "Element",
        }
    )
    max_length: List[MaxLength] = field(
        default_factory=list,
        metadata={
            "name": "maxLength",
            "type": "Element",
        }
    )
    enumeration: List[Enumeration] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    white_space: List[WhiteSpace] = field(
        default_factory=list,
        metadata={
            "name": "whiteSpace",
            "type": "Element",
        }
    )
    pattern: List[Pattern] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    base: Optional[QName] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class UnionType(Annotated):
    class Meta:
        name = "union"
        namespace = "http://www.w3.org/2001/XMLSchema"

    simple_type: List["LocalSimpleType"] = field(
        default_factory=list,
        metadata={
            "name": "simpleType",
            "type": "Element",
        }
    )
    member_types: List[QName] = field(
        default_factory=list,
        metadata={
            "name": "memberTypes",
            "type": "Attribute",
            "tokens": True,
        }
    )


@dataclass
class SimpleType1(Annotated):
    """
    :ivar restriction:
    :ivar list_value:
    :ivar union:
    :ivar final:
    :ivar name: Can be restricted to required or forbidden
    """
    class Meta:
        name = "simpleType"

    restriction: Optional[Restriction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    list_value: Optional[ListType] = field(
        default=None,
        metadata={
            "name": "list",
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    union: Optional[UnionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    final: Optional[SimpleDerivationSet] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class LocalSimpleType(SimpleType1):
    class Meta:
        name = "localSimpleType"
