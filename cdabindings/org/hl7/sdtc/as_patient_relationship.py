from dataclasses import dataclass
from cdabindings.org.hl7.sdtc.as_patient_relationship_1 import AsPatientRelationship1

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class AsPatientRelationship(AsPatientRelationship1):
    class Meta:
        name = "asPatientRelationship"
        namespace = "urn:hl7-org:sdtc"
