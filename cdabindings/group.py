from dataclasses import dataclass

from cdabindings.named_group import NamedGroup

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Group(NamedGroup):
    class Meta:
        name = "group"
        namespace = "http://www.w3.org/2001/XMLSchema"
