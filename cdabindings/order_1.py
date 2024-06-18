from dataclasses import dataclass, field

__NAMESPACE__ = "urn:dicom-org:ps3-20"


@dataclass
class Order1:
    class Meta:
        name = "POCD_MT000040.Order"

    id: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:dicom-org:ps3-20",
            "min_occurs": 1,
        },
    )
    accession_number: list[str] = field(
        default_factory=list,
        metadata={
            "name": "accessionNumber",
            "type": "Element",
            "namespace": "urn:dicom-org:ps3-20",
        },
    )
