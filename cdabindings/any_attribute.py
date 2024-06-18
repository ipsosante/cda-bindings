from dataclasses import dataclass

from cdabindings.wildcard import Wildcard

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class AnyAttribute(Wildcard):
    class Meta:
        name = "anyAttribute"
        namespace = "http://www.w3.org/2001/XMLSchema"
