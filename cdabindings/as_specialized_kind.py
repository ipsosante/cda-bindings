from dataclasses import dataclass

from cdabindings.coct_mt230100_uv_specialized_kind import (
    CoctMt230100UvSpecializedKind,
)

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class AsSpecializedKind(CoctMt230100UvSpecializedKind):
    class Meta:
        name = "asSpecializedKind"
        nillable = True
        namespace = "urn:ihe:pharm:medication"
