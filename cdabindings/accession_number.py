from dataclasses import dataclass

__NAMESPACE__ = "urn:dicom-org:ps3-20"


@dataclass
class AccessionNumber:
    class Meta:
        name = "accessionNumber"
        namespace = "urn:dicom-org:ps3-20"
