from dataclasses import dataclass

from cdabindings.coct_mt230100_uv_medication import CoctMt230100UvMedication

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class Medication(CoctMt230100UvMedication):
    class Meta:
        name = "medication"
        namespace = "urn:ihe:pharm:medication"
