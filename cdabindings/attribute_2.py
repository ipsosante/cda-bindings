from dataclasses import dataclass

from cdabindings.top_level_attribute import TopLevelAttribute

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Attribute2(TopLevelAttribute):
    class Meta:
        name = "attribute"
        namespace = "http://www.w3.org/2001/XMLSchema"
