from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union
from cda.org.hl7.v3.cr import CV

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Pqr(CV):
    """A representation of a physical quantity in a unit from any code system.

    Used to show alternative representation for a physical quantity.

    :ivar value: The magnitude of the measurement value in terms of the
        unit specified in the code.
    """
    class Meta:
        name = "PQR"

    value: Optional[Union[Decimal, float]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
