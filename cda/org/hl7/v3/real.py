from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union
from cda.org.hl7.v3.qty import Qty

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Real(Qty):
    """Fractional numbers.

    Typically used whenever quantities are measured, estimated, or
    computed from other real numbers.  The typical representation is
    decimal, where the number of significant decimal digits is known as
    the precision. Real numbers are needed beyond integers whenever
    quantities of the real world are measured, estimated, or computed
    from other real numbers. The term "Real number" in this
    specification is used to mean that fractional values are covered
    without necessarily implying the full set of the mathematical real
    numbers.
    """
    class Meta:
        name = "REAL"

    value: Optional[Union[Decimal, float]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
