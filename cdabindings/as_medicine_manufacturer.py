from dataclasses import dataclass

from cdabindings.coct_mt230100_uv_medicine_manufacturer import (
    CoctMt230100UvMedicineManufacturer,
)

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class AsMedicineManufacturer(CoctMt230100UvMedicineManufacturer):
    class Meta:
        name = "asMedicineManufacturer"
        nillable = True
        namespace = "urn:ihe:pharm:medication"
