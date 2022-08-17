from dataclasses import dataclass, field
from cda.org.hl7.v3.cr import CE

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class EivlEvent(CE):
    """
    A code for a common (periodical) activity of daily living based on which
    the event related periodic interval is specified.
    """
    class Meta:
        name = "EIVL.event"

    code_system: str = field(
        init=False,
        default="2.16.840.1.113883.5.139",
        metadata={
            "name": "codeSystem",
            "type": "Attribute",
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    code_system_name: str = field(
        init=False,
        default="TimingEvent",
        metadata={
            "name": "codeSystemName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
