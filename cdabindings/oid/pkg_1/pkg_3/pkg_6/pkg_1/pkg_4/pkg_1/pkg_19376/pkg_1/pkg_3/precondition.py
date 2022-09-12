from dataclasses import dataclass, field
from typing import Optional
from cdabindings.oid.pkg_1.pkg_3.pkg_6.pkg_1.pkg_4.pkg_1.pkg_19376.pkg_1.pkg_3.criterion import Criterion
from cdabindings.oid.pkg_1.pkg_3.pkg_6.pkg_1.pkg_4.pkg_1.pkg_19376.pkg_1.pkg_3.precondition_type_code import PreconditionTypeCode

__NAMESPACE__ = "urn:oid:1.3.6.1.4.1.19376.1.3.2"


@dataclass
class Precondition:
    class Meta:
        name = "precondition"
        namespace = "urn:oid:1.3.6.1.4.1.19376.1.3.2"

    criterion: Optional[Criterion] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    type_code: Optional[PreconditionTypeCode] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
