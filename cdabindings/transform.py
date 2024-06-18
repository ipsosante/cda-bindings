from dataclasses import dataclass, field
from typing import Optional

from cdabindings.attribute_set import AttributeSet
from cdabindings.character_map import CharacterMap
from cdabindings.decimal_format import DecimalFormat
from cdabindings.function import Function
from cdabindings.import_2 import Import2
from cdabindings.import_schema import ImportSchema
from cdabindings.include_2 import Include2
from cdabindings.input_type_annotations_type import InputTypeAnnotationsType
from cdabindings.key_2 import Key2
from cdabindings.namespace_alias import NamespaceAlias
from cdabindings.output import Output
from cdabindings.param import Param
from cdabindings.preserve_space import PreserveSpace
from cdabindings.strip_space import StripSpace
from cdabindings.template import Template
from cdabindings.transform_element_base_type import TransformElementBaseType
from cdabindings.validation_strip_or_preserve import ValidationStripOrPreserve
from cdabindings.variable import Variable

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Transform(TransformElementBaseType):
    class Meta:
        name = "transform"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    import_value: list[Import2] = field(
        default_factory=list,
        metadata={
            "name": "import",
            "type": "Element",
        },
    )
    template: list[Template] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    strip_space: list[StripSpace] = field(
        default_factory=list,
        metadata={
            "name": "strip-space",
            "type": "Element",
        },
    )
    preserve_space: list[PreserveSpace] = field(
        default_factory=list,
        metadata={
            "name": "preserve-space",
            "type": "Element",
        },
    )
    output: list[Output] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    namespace_alias: list[NamespaceAlias] = field(
        default_factory=list,
        metadata={
            "name": "namespace-alias",
            "type": "Element",
        },
    )
    key: list[Key2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    include: list[Include2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    import_schema: list[ImportSchema] = field(
        default_factory=list,
        metadata={
            "name": "import-schema",
            "type": "Element",
        },
    )
    function: list[Function] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    decimal_format: list[DecimalFormat] = field(
        default_factory=list,
        metadata={
            "name": "decimal-format",
            "type": "Element",
        },
    )
    character_map: list[CharacterMap] = field(
        default_factory=list,
        metadata={
            "name": "character-map",
            "type": "Element",
        },
    )
    attribute_set: list[AttributeSet] = field(
        default_factory=list,
        metadata={
            "name": "attribute-set",
            "type": "Element",
        },
    )
    variable: list[Variable] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    param: list[Param] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    default_validation: ValidationStripOrPreserve = field(
        default=ValidationStripOrPreserve.STRIP,
        metadata={
            "name": "default-validation",
            "type": "Attribute",
        },
    )
    input_type_annotations: InputTypeAnnotationsType = field(
        default=InputTypeAnnotationsType.UNSPECIFIED,
        metadata={
            "name": "input-type-annotations",
            "type": "Attribute",
        },
    )
