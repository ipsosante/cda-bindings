from dataclasses import dataclass, field
from typing import Optional
from cdabindings.org.hl7.v3.eivl_event import EivlEvent
from cdabindings.org.hl7.v3.ivl_ppd_pq import IvlPpdPq
from cdabindings.org.hl7.v3.sxcm_ppd_ts import SxcmPpdTs

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class EivlPpdTs(SxcmPpdTs):
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
        name = "EIVL_PPD_TS"

    event: Optional[EivlEvent] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    offset: Optional[IvlPpdPq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
