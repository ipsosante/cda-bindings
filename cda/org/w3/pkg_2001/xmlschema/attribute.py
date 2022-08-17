from dataclasses import dataclass
from cda.org.w3.pkg_2001.xmlschema.top_level_attribute import TopLevelAttribute

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Attribute(TopLevelAttribute):
    class Meta:
        name = "attribute"
        namespace = "http://www.w3.org/2001/XMLSchema"
