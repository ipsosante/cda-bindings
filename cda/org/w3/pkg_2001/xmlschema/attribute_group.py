from dataclasses import dataclass
from cda.org.w3.pkg_2001.xmlschema.named_attribute_group import NamedAttributeGroup

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class AttributeGroup(NamedAttributeGroup):
    class Meta:
        name = "attributeGroup"
        namespace = "http://www.w3.org/2001/XMLSchema"
