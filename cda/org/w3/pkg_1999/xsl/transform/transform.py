from dataclasses import dataclass, field
from typing import List, Optional
from cda.org.w3.pkg_1999.xsl.transform.attribute_set import AttributeSet
from cda.org.w3.pkg_1999.xsl.transform.character_map import CharacterMap
from cda.org.w3.pkg_1999.xsl.transform.decimal_format import DecimalFormat
from cda.org.w3.pkg_1999.xsl.transform.function import Function
from cda.org.w3.pkg_1999.xsl.transform.import_mod import Import
from cda.org.w3.pkg_1999.xsl.transform.import_schema import ImportSchema
from cda.org.w3.pkg_1999.xsl.transform.include import Include
from cda.org.w3.pkg_1999.xsl.transform.input_type_annotations_type import InputTypeAnnotationsType
from cda.org.w3.pkg_1999.xsl.transform.key import Key
from cda.org.w3.pkg_1999.xsl.transform.namespace_alias import NamespaceAlias
from cda.org.w3.pkg_1999.xsl.transform.output import Output
from cda.org.w3.pkg_1999.xsl.transform.param import Param
from cda.org.w3.pkg_1999.xsl.transform.preserve_space import PreserveSpace
from cda.org.w3.pkg_1999.xsl.transform.strip_space import StripSpace
from cda.org.w3.pkg_1999.xsl.transform.template import Template
from cda.org.w3.pkg_1999.xsl.transform.transform_element_base_type import TransformElementBaseType
from cda.org.w3.pkg_1999.xsl.transform.validation_strip_or_preserve import ValidationStripOrPreserve
from cda.org.w3.pkg_1999.xsl.transform.variable import Variable

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Transform(TransformElementBaseType):
    class Meta:
        name = "transform"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    import_value: List[Import] = field(
        default_factory=list,
        metadata={
            "name": "import",
            "type": "Element",
        }
    )
    template: List[Template] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    strip_space: List[StripSpace] = field(
        default_factory=list,
        metadata={
            "name": "strip-space",
            "type": "Element",
            "sequential": True,
        }
    )
    preserve_space: List[PreserveSpace] = field(
        default_factory=list,
        metadata={
            "name": "preserve-space",
            "type": "Element",
            "sequential": True,
        }
    )
    output: List[Output] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    namespace_alias: List[NamespaceAlias] = field(
        default_factory=list,
        metadata={
            "name": "namespace-alias",
            "type": "Element",
            "sequential": True,
        }
    )
    key: List[Key] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    include: List[Include] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    import_schema: List[ImportSchema] = field(
        default_factory=list,
        metadata={
            "name": "import-schema",
            "type": "Element",
            "sequential": True,
        }
    )
    function: List[Function] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    decimal_format: List[DecimalFormat] = field(
        default_factory=list,
        metadata={
            "name": "decimal-format",
            "type": "Element",
            "sequential": True,
        }
    )
    character_map: List[CharacterMap] = field(
        default_factory=list,
        metadata={
            "name": "character-map",
            "type": "Element",
            "sequential": True,
        }
    )
    attribute_set: List[AttributeSet] = field(
        default_factory=list,
        metadata={
            "name": "attribute-set",
            "type": "Element",
            "sequential": True,
        }
    )
    variable: List[Variable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    param: List[Param] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
            "sequential": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    default_validation: ValidationStripOrPreserve = field(
        default=ValidationStripOrPreserve.STRIP,
        metadata={
            "name": "default-validation",
            "type": "Attribute",
        }
    )
    input_type_annotations: InputTypeAnnotationsType = field(
        default=InputTypeAnnotationsType.UNSPECIFIED,
        metadata={
            "name": "input-type-annotations",
            "type": "Attribute",
        }
    )
