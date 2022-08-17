from dataclasses import dataclass
from cda.org.w3.pkg_2001.xmlschema.wildcard import Wildcard

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class AnyAttribute(Wildcard):
    class Meta:
        name = "anyAttribute"
        namespace = "http://www.w3.org/2001/XMLSchema"
