from dataclasses import dataclass

from cdabindings.coct_mt230100_uv_content import CoctMt230100UvContent

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class AsContent(CoctMt230100UvContent):
    class Meta:
        name = "asContent"
        nillable = True
        namespace = "urn:ihe:pharm:medication"
