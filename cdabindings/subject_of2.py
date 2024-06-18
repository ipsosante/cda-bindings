from dataclasses import dataclass

from cdabindings.coct_mt230100_uv_subject1 import CoctMt230100UvSubject1

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class SubjectOf2(CoctMt230100UvSubject1):
    class Meta:
        name = "subjectOf2"
        nillable = True
        namespace = "urn:ihe:pharm:medication"
