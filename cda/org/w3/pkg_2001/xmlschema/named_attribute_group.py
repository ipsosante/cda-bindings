from dataclasses import dataclass
from cda.org.w3.pkg_2001.xmlschema.attribute_group_1 import AttributeGroup1

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class NamedAttributeGroup(AttributeGroup1):
    class Meta:
        name = "namedAttributeGroup"
