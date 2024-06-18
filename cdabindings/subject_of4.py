from dataclasses import dataclass

from cdabindings.coct_mt230100_uv_subject3 import CoctMt230100UvSubject3

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class SubjectOf4(CoctMt230100UvSubject3):
    class Meta:
        name = "subjectOf4"
        nillable = True
        namespace = "urn:ihe:pharm:medication"
