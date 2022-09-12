from dataclasses import dataclass, field
from typing import List
from cdabindings.org.hl7.v3.sxcm_ts import SxcmTs
from cdabindings.org.hl7.v3.telecommunication_address_use import TelecommunicationAddressUse
from cdabindings.org.hl7.v3.url import Url

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Tel(Url):
    """A telephone number (voice or fax), e-mail address, or other locator for
    a resource (information or service) mediated by telecommunication
    equipment.

    The address is specified as a URL qualified by time specification
    and use codes that help in deciding which address to use for a given
    time and purpose.

    :ivar useable_period: Specifies the periods of time during which the
        telecommunication address can be used.  For a telephone number,
        this can indicate the time of day in which the party can be
        reached on that telephone. For a web address, it may specify a
        time range in which the web content is promised to be available
        under the given address.
    :ivar use: One or more codes advising a system or user which
        telecommunication address in a set of like addresses to select
        for a given telecommunication need.
    """
    class Meta:
        name = "TEL"

    useable_period: List[SxcmTs] = field(
        default_factory=list,
        metadata={
            "name": "useablePeriod",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    use: List[TelecommunicationAddressUse] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
