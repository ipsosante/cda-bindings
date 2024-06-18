from dataclasses import dataclass

from cdabindings.named_attribute_group import NamedAttributeGroup

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class AttributeGroup(NamedAttributeGroup):
    class Meta:
        name = "attributeGroup"
        namespace = "http://www.w3.org/2001/XMLSchema"
