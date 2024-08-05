from dataclasses import dataclass, field
from typing import Optional

from cdabindings.act_clinical_document import ActClinicalDocument
from cdabindings.act_mood import ActMood
from cdabindings.authenticator import Authenticator
from cdabindings.author import Author
from cdabindings.authorization import Authorization
from cdabindings.ce import CE
from cdabindings.component1 import Component1
from cdabindings.component2 import Component2
from cdabindings.cs import CS
from cdabindings.custodian import Custodian
from cdabindings.data_enterer import DataEnterer
from cdabindings.documentation_of import DocumentationOf
from cdabindings.ii import II
from cdabindings.in_fulfillment_of import InFulfillmentOf
from cdabindings.informant12 import Informant12
from cdabindings.information_recipient import InformationRecipient
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.int_mod import Int
from cdabindings.legal_authenticator import LegalAuthenticator
from cdabindings.null_flavor import NullFlavor
from cdabindings.participant1 import Participant1
from cdabindings.record_target import RecordTarget
from cdabindings.related_document import RelatedDocument
from cdabindings.st import ST
from cdabindings.status_code_1 import StatusCode1
from cdabindings.ts import TS

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class BaseClinicalDocument:
    class Meta:
        name = "POCD_MT000040.ClinicalDocument"

    realm_code: list[CS] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[InfrastructureRootTypeId] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    template_id: list[II] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: Optional[II] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    code: Optional[CE] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    title: Optional[ST] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: Optional[TS] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    confidentiality_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "confidentialityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    language_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    set_id: Optional[II] = field(
        default=None,
        metadata={
            "name": "setId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    version_number: Optional[Int] = field(
        default=None,
        metadata={
            "name": "versionNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    copy_time: Optional[TS] = field(
        default=None,
        metadata={
            "name": "copyTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    record_target: list[RecordTarget] = field(
        default_factory=list,
        metadata={
            "name": "recordTarget",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    author: list[Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    data_enterer: Optional[DataEnterer] = field(
        default=None,
        metadata={
            "name": "dataEnterer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    informant: list[Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    custodian: Optional[Custodian] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    information_recipient: list[InformationRecipient] = field(
        default_factory=list,
        metadata={
            "name": "informationRecipient",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    legal_authenticator: Optional[LegalAuthenticator] = field(
        default=None,
        metadata={
            "name": "legalAuthenticator",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    authenticator: list[Authenticator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    participant: list[Participant1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    in_fulfillment_of: list[InFulfillmentOf] = field(
        default_factory=list,
        metadata={
            "name": "inFulfillmentOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    documentation_of: list[DocumentationOf] = field(
        default_factory=list,
        metadata={
            "name": "documentationOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    related_document: list[RelatedDocument] = field(
        default_factory=list,
        metadata={
            "name": "relatedDocument",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    authorization: list[Authorization] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    component_of: Optional[Component1] = field(
        default=None,
        metadata={
            "name": "componentOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    component: Optional[Component2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    status_code: Optional[StatusCode1] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: ActClinicalDocument = field(
        init=False,
        default=ActClinicalDocument.DOCCLIN,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
        },
    )


@dataclass
class ClinicalDocument(BaseClinicalDocument):
    class Meta:
        namespace = "urn:hl7-org:v3"
