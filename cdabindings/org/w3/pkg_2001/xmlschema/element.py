from dataclasses import dataclass
from cdabindings.org.w3.pkg_2001.xmlschema.top_level_element import TopLevelElement

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Element(TopLevelElement):
    class Meta:
        name = "element"
        namespace = "http://www.w3.org/2001/XMLSchema"
