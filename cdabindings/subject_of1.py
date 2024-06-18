from dataclasses import dataclass

from cdabindings.coct_mt230100_uv_subject2 import CoctMt230100UvSubject2

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class SubjectOf1(CoctMt230100UvSubject2):
    class Meta:
        name = "subjectOf1"
        nillable = True
        namespace = "urn:ihe:pharm:medication"
