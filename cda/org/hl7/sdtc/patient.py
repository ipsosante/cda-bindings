from dataclasses import dataclass
from cda.org.hl7.sdtc.sdtc_patient import SdtcPatient

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class Patient(SdtcPatient):
    class Meta:
        name = "patient"
        namespace = "urn:hl7-org:sdtc"
