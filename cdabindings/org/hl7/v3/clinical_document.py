from dataclasses import dataclass, field
from typing import List, Optional
from cdabindings.org.hl7.sdtc.status_code import StatusCode
from cdabindings.org.hl7.v3.act_clinical_document import ActClinicalDocument
from cdabindings.org.hl7.v3.act_mood import ActMood
from cdabindings.org.hl7.v3.authenticator import Authenticator
from cdabindings.org.hl7.v3.author import Author
from cdabindings.org.hl7.v3.authorization import Authorization
from cdabindings.org.hl7.v3.component1 import Component1
from cdabindings.org.hl7.v3.component2 import Component2
from cdabindings.org.hl7.v3.cr import CE
from cdabindings.org.hl7.v3.cs import CS
from cdabindings.org.hl7.v3.custodian import Custodian
from cdabindings.org.hl7.v3.data_enterer import DataEnterer
from cdabindings.org.hl7.v3.documentation_of import DocumentationOf
from cdabindings.org.hl7.v3.ii import II
from cdabindings.org.hl7.v3.in_fulfillment_of import InFulfillmentOf
from cdabindings.org.hl7.v3.informant12 import Informant12
from cdabindings.org.hl7.v3.information_recipient import InformationRecipient
from cdabindings.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.org.hl7.v3.int_mod import Int
from cdabindings.org.hl7.v3.legal_authenticator import LegalAuthenticator
from cdabindings.org.hl7.v3.null_flavor import NullFlavor
from cdabindings.org.hl7.v3.participant1 import Participant1
from cdabindings.org.hl7.v3.record_target import RecordTarget
from cdabindings.org.hl7.v3.related_document import RelatedDocument
from cdabindings.org.hl7.v3.st import ST
from cdabindings.org.hl7.v3.ts import TS

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class ClinicalDocument:
    class Meta:
        name = "POCD_MT000040.ClinicalDocument"

    realm_code: List[CS] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[InfrastructureRootTypeId] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    template_id: List[II] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[II] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    code: Optional[CE] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    title: Optional[ST] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[StatusCode] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    effective_time: Optional[TS] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    confidentiality_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "confidentialityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    language_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    set_id: Optional[II] = field(
        default=None,
        metadata={
            "name": "setId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    version_number: Optional[Int] = field(
        default=None,
        metadata={
            "name": "versionNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    copy_time: Optional[TS] = field(
        default=None,
        metadata={
            "name": "copyTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    record_target: List[RecordTarget] = field(
        default_factory=list,
        metadata={
            "name": "recordTarget",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    author: List[Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    data_enterer: Optional[DataEnterer] = field(
        default=None,
        metadata={
            "name": "dataEnterer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    custodian: Optional[Custodian] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    information_recipient: List[InformationRecipient] = field(
        default_factory=list,
        metadata={
            "name": "informationRecipient",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    legal_authenticator: Optional[LegalAuthenticator] = field(
        default=None,
        metadata={
            "name": "legalAuthenticator",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    authenticator: List[Authenticator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[Participant1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    in_fulfillment_of: List[InFulfillmentOf] = field(
        default_factory=list,
        metadata={
            "name": "inFulfillmentOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    documentation_of: List[DocumentationOf] = field(
        default_factory=list,
        metadata={
            "name": "documentationOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    related_document: List[RelatedDocument] = field(
        default_factory=list,
        metadata={
            "name": "relatedDocument",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    authorization: List[Authorization] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    component_of: Optional[Component1] = field(
        default=None,
        metadata={
            "name": "componentOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    component: Optional[Component2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClinicalDocument = field(
        init=False,
        default=ActClinicalDocument.DOCCLIN,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
        }
    )


@dataclass
class ClinicalDocument(ClinicalDocument):
    class Meta:
        namespace = "urn:hl7-org:v3"
