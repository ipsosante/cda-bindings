from dataclasses import dataclass

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class FormCode:
    class Meta:
        name = "formCode"
        namespace = "urn:ihe:pharm:medication"
