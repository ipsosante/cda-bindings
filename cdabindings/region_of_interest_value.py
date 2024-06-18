from dataclasses import dataclass, field

from cdabindings.int_mod import Int

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class RegionOfInterestValue(Int):
    class Meta:
        name = "POCD_MT000040.RegionOfInterest.value"

    unsorted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
