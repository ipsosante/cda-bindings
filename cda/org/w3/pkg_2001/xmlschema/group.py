from dataclasses import dataclass
from cda.org.w3.pkg_2001.xmlschema.named_group import NamedGroup

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Group(NamedGroup):
    class Meta:
        name = "group"
        namespace = "http://www.w3.org/2001/XMLSchema"
