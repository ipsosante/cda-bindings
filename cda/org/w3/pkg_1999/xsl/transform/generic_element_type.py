from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union
from cda.org.w3.pkg_1999.xsl.transform.prefix_list_or_all_value import PrefixListOrAllValue
from cda.org.w3.pkg_1999.xsl.transform.prefix_or_default_value import PrefixOrDefaultValue

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class GenericElementType:
    class Meta:
        name = "generic-element-type"

    default_collation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "default-collation",
            "type": "Attribute",
            "tokens": True,
        }
    )
    exclude_result_prefixes: List[Union[str, PrefixOrDefaultValue, PrefixListOrAllValue]] = field(
        default_factory=list,
        metadata={
            "name": "exclude-result-prefixes",
            "type": "Attribute",
            "tokens": True,
        }
    )
    extension_element_prefixes: List[Union[str, PrefixOrDefaultValue]] = field(
        default_factory=list,
        metadata={
            "name": "extension-element-prefixes",
            "type": "Attribute",
            "tokens": True,
        }
    )
    use_when: Optional[str] = field(
        default=None,
        metadata={
            "name": "use-when",
            "type": "Attribute",
            "pattern": r".+",
        }
    )
    xpath_default_namespace: Optional[str] = field(
        default=None,
        metadata={
            "name": "xpath-default-namespace",
            "type": "Attribute",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
