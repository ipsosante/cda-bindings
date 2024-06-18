from dataclasses import dataclass

__NAMESPACE__ = "urn:dicom-org:ps3-20"


@dataclass
class Id3:
    class Meta:
        name = "id"
        namespace = "urn:dicom-org:ps3-20"
