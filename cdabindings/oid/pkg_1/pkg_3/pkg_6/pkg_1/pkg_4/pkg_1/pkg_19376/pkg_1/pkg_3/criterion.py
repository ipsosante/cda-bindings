from dataclasses import dataclass, field
from typing import Optional
from cdabindings.oid.pkg_1.pkg_3.pkg_6.pkg_1.pkg_4.pkg_1.pkg_19376.pkg_1.pkg_3.code import Code
from cdabindings.oid.pkg_1.pkg_3.pkg_6.pkg_1.pkg_4.pkg_1.pkg_19376.pkg_1.pkg_3.criterion_class_code import CriterionClassCode
from cdabindings.oid.pkg_1.pkg_3.pkg_6.pkg_1.pkg_4.pkg_1.pkg_19376.pkg_1.pkg_3.criterion_mood_code import CriterionMoodCode
from cdabindings.oid.pkg_1.pkg_3.pkg_6.pkg_1.pkg_4.pkg_1.pkg_19376.pkg_1.pkg_3.value import Value

__NAMESPACE__ = "urn:oid:1.3.6.1.4.1.19376.1.3.2"


@dataclass
class Criterion:
    code: Optional[Code] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oid:1.3.6.1.4.1.19376.1.3.2",
        }
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:oid:1.3.6.1.4.1.19376.1.3.2",
        }
    )
    class_code: Optional[CriterionClassCode] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    mood_code: Optional[CriterionMoodCode] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
        }
    )
