from dataclasses import dataclass, field
from typing import Optional, Union
from cda.org.w3.pkg_1999.xsl.transform.element_only_versioned_element_type import ElementOnlyVersionedElementType
from cda.org.w3.pkg_1999.xsl.transform.prefix_or_default_value import PrefixOrDefaultValue

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class NamespaceAlias(ElementOnlyVersionedElementType):
    class Meta:
        name = "namespace-alias"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    stylesheet_prefix: Optional[Union[str, PrefixOrDefaultValue]] = field(
        default=None,
        metadata={
            "name": "stylesheet-prefix",
            "type": "Attribute",
            "required": True,
        }
    )
    result_prefix: Optional[Union[str, PrefixOrDefaultValue]] = field(
        default=None,
        metadata={
            "name": "result-prefix",
            "type": "Attribute",
            "required": True,
        }
    )
