from dataclasses import dataclass

from cdabindings.coct_mt230100_uv_subject22 import CoctMt230100UvSubject22

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class SubjectOf3(CoctMt230100UvSubject22):
    class Meta:
        name = "subjectOf3"
        nillable = True
        namespace = "urn:ihe:pharm:medication"
