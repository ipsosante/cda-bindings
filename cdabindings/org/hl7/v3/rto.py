from dataclasses import dataclass
from cdabindings.org.hl7.v3.rto_qty_qty import RtoQtyQty

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Rto(RtoQtyQty):
    """A quantity constructed as the quotient of a numerator quantity divided
    by a denominator quantity.

    Common factors in the numerator and denominator are not
    automatically cancelled out.   supports titers (e.g., "1:128") and
    other quantities produced by laboratories that truly represent
    ratios. Ratios are not simply "structured numerics", particularly
    blood pressure measurements (e.g. "120/60") are not ratios. In many
    cases REAL should be used instead of .
    """
    class Meta:
        name = "RTO"
