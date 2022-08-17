from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union
from cda.org.hl7.v3.qty import Qty

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Mo(Qty):
    """A monetary amount is a quantity expressing the amount of money in some
    currency.

    Currencies are the units in which monetary amounts are denominated
    in different economic regions. While the monetary amount is a single
    kind of quantity (money) the exchange rates between the different
    units are variable.  This is the principle difference between
    physical quantity and monetary amounts, and the reason why currency
    units are not physical units.

    :ivar value: The magnitude of the monetary amount in terms of the
        currency unit.
    :ivar currency: The currency unit as defined in ISO 4217.
    """
    class Meta:
        name = "MO"

    value: Optional[Union[Decimal, float]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
