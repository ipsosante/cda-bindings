from dataclasses import dataclass
from cda.org.w3.pkg_2001.xmlschema.keybase import Keybase

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Key(Keybase):
    class Meta:
        name = "key"
        namespace = "http://www.w3.org/2001/XMLSchema"
