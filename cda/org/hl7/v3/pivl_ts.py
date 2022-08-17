from dataclasses import dataclass, field
from typing import Optional, Union
from cda.org.hl7.v3.calendar_cycle_one_letter import CalendarCycleOneLetter
from cda.org.hl7.v3.calendar_cycle_two_letter_value import CalendarCycleTwoLetterValue
from cda.org.hl7.v3.ivl_ts import IvlTs
from cda.org.hl7.v3.pq import Pq
from cda.org.hl7.v3.sxcm_ts import SxcmTs

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class PivlTs(SxcmTs):
    """Note: because this type is defined as an extension of SXCM_T,
    all of the attributes and elements accepted for T are also
    accepted by this definition.  However, they are NOT allowed
    by the normative description of this type.  Unfortunately,
    we cannot write a general purpose schematron contraints to
    provide that extra validation, thus applications must be
    aware that instance (fragments) that pass validation with
    this might might still not be legal.

    :ivar phase: A prototype of the repeating interval specifying the
        duration of each occurrence and anchors the periodic interval
        sequence at a certain point in time.
    :ivar period: A time duration specifying a reciprocal measure of the
        frequency at which the periodic interval repeats.
    :ivar alignment: Specifies if and how the repetitions are aligned to
        the cycles of the underlying calendar (e.g., to distinguish
        every 30 days from "the 5th of every month".) A non-aligned
        periodic interval recurs independently from the calendar. An
        aligned periodic interval is synchronized with the calendar.
    :ivar institution_specified: Indicates whether the exact timing is
        up to the party executing the schedule (e.g., to distinguish
        "every 8 hours" from "3 times a day".)
    """
    class Meta:
        name = "PIVL_TS"

    phase: Optional[IvlTs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    period: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    alignment: Optional[Union[CalendarCycleOneLetter, str, CalendarCycleTwoLetterValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )
    institution_specified: str = field(
        default="false",
        metadata={
            "name": "institutionSpecified",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )
