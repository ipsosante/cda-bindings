from dataclasses import dataclass, field
from typing import Optional
from cda.org.hl7.v3.qty import Qty

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class TS(Qty):
    """A quantity specifying a point on the axis of natural time.

    A point in time is most often represented as a calendar expression.
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}|([0-9]{9,14}|[0-9]{14,14}\.[0-9]+)([+\-][0-9]{1,4})?",
        }
    )
