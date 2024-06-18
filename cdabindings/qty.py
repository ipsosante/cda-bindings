from dataclasses import dataclass

from cdabindings.any_abstract import AnyAbstract

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Qty(AnyAbstract):
    """The quantity data type is an abstract generalization for all data types (1)
    whose value set has an order relation (less-or-equal) and (2) where difference
    is defined in all of the data type's totally ordered value subsets.

    The quantity type abstraction is needed in defining certain other
    types, such as the interval and the probability distribution.
    """

    class Meta:
        name = "QTY"
