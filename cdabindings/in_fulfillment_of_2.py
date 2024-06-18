from dataclasses import dataclass, field
from typing import Optional

from cdabindings.order_1 import Order1

__NAMESPACE__ = "urn:dicom-org:ps3-20"


@dataclass
class InFulfillmentOf2:
    class Meta:
        name = "InFulfillmentOf"

    order: Optional[Order1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:dicom-org:ps3-20",
            "required": True,
        },
    )
