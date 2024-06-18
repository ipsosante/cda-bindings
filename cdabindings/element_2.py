from dataclasses import dataclass

from cdabindings.top_level_element import TopLevelElement

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Element2(TopLevelElement):
    class Meta:
        name = "element"
        namespace = "http://www.w3.org/2001/XMLSchema"
