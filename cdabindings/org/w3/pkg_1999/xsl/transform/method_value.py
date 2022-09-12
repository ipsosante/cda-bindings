from enum import Enum

__NAMESPACE__ = "http://www.w3.org/1999/XSL/Transform"


class MethodValue(Enum):
    XML = "xml"
    XHTML = "xhtml"
    HTML = "html"
    TEXT = "text"
