from dataclasses import dataclass, field
from typing import Optional
from cdabindings.oid.pkg_1.pkg_3.pkg_6.pkg_1.pkg_4.pkg_1.pkg_19376.pkg_1.pkg_3.value_value import ValueValue

__NAMESPACE__ = "urn:oid:1.3.6.1.4.1.19376.1.3.2"


@dataclass
class Value:
    value: Optional[ValueValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
