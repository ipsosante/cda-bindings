from dataclasses import dataclass

from cdabindings.coct_mt230100_uv_ingredient import CoctMt230100UvIngredient

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class Ingredient(CoctMt230100UvIngredient):
    class Meta:
        name = "ingredient"
        nillable = True
        namespace = "urn:ihe:pharm:medication"
