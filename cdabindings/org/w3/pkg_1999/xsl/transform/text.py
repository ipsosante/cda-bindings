from dataclasses import dataclass, field
from cdabindings.org.w3.pkg_1999.xsl.transform.text_element_base_type import TextElementBaseType
from cdabindings.org.w3.pkg_1999.xsl.transform.yes_or_no import YesOrNo

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


@dataclass
class Text(TextElementBaseType):
    class Meta:
        name = "text"
        namespace = "http://www.w3.org/1999/XSL/Transform"

    disable_output_escaping: YesOrNo = field(
        default=YesOrNo.NO,
        metadata={
            "name": "disable-output-escaping",
            "type": "Attribute",
        }
    )
