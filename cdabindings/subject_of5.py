from dataclasses import dataclass

from cdabindings.coct_mt230100_uv_subject7 import CoctMt230100UvSubject7

__NAMESPACE__ = "urn:ihe:pharm:medication"


@dataclass
class SubjectOf5(CoctMt230100UvSubject7):
    class Meta:
        name = "subjectOf5"
        nillable = True
        namespace = "urn:ihe:pharm:medication"
