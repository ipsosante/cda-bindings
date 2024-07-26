from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from cdabindings.pqr import PQR
from cdabindings.qty import Qty

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class PQ(Qty):
    """
    A dimensioned quantity expressing the result of a measurement act.

    :ivar translation: An alternative representation of the same
        physical quantity expressed in a different unit, of a different
        unit code system and possibly with a different value.
    :ivar value: The magnitude of the quantity measured in terms of the
        unit.
    :ivar unit: The unit of measure specified in the Unified Code for
        Units of Measure (UCUM) [http://aurora.rg.iupui.edu/UCUM].
    """

    translation: list[PQR] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    value: Optional[Union[Decimal, float]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    unit: str = field(
        default="1",
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        },
    )
