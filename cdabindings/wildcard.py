from dataclasses import dataclass, field

from cdabindings.annotated import Annotated
from cdabindings.namespace_list import NamespaceList
from cdabindings.wildcard_process_contents import WildcardProcessContents

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Wildcard(Annotated):
    class Meta:
        name = "wildcard"

    namespace: NamespaceList = field(
        default=NamespaceList.ANY,
        metadata={
            "type": "Attribute",
        },
    )
    process_contents: WildcardProcessContents = field(
        default=WildcardProcessContents.STRICT,
        metadata={
            "name": "processContents",
            "type": "Attribute",
        },
    )
