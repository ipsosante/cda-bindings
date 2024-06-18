from dataclasses import dataclass, field
from typing import Optional

from cdabindings.eivl_event import EivlEvent
from cdabindings.ivl_pq import IvlPq
from cdabindings.sxcm_ts import SxcmTs

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class EivlTs(SxcmTs):
    """Note: because this type is defined as an extension of SXCM_T,
    all of the attributes and elements accepted for T are also
    accepted by this definition.  However, they are NOT allowed
    by the normative description of this type.  Unfortunately,
    we cannot write a general purpose schematron contraints to
    provide that extra validation, thus applications must be
    aware that instance (fragments) that pass validation with
    this might might still not be legal.

    :ivar event: A code for a common (periodical) activity of daily
        living based on which the event related periodic interval is
        specified.
    :ivar offset: An interval of elapsed time (duration, not absolute
        point in time) that marks the offsets for the beginning, width
        and end of the event-related periodic interval measured from the
        time each such event actually occurred.
    """

    class Meta:
        name = "EIVL_TS"

    event: Optional[EivlEvent] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    offset: Optional[IvlPq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
