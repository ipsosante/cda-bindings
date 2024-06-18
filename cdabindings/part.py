from dataclasses import dataclass

from cdabindings.coct_mt230100_uv_medicine import CoctMt230100UvPart

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class Part(CoctMt230100UvPart):
    class Meta:
        name = "part"
        nillable = True
        namespace = "urn:ihe:pharm:medication"
