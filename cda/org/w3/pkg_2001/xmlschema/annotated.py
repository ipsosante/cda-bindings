from dataclasses import dataclass, field
from typing import Optional
from cda.org.w3.pkg_2001.xmlschema.annotation import Annotation
from cda.org.w3.pkg_2001.xmlschema.open_attrs import OpenAttrs

__NAMESPACE__ = "http://www.w3.org/2001/XMLSchema"


@dataclass
class Annotated(OpenAttrs):
    """
    This type is extended by all types which allow annotation other than
    &lt;schema&gt; itself.
    """
    class Meta:
        name = "annotated"

    annotation: Optional[Annotation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2001/XMLSchema",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
