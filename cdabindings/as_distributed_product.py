from dataclasses import dataclass

from cdabindings.coct_mt230100_uv_distributed_product import (
    CoctMt230100UvDistributedProduct,
)

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class AsDistributedProduct(CoctMt230100UvDistributedProduct):
    class Meta:
        name = "asDistributedProduct"
        nillable = True
        namespace = "urn:ihe:pharm:medication"
