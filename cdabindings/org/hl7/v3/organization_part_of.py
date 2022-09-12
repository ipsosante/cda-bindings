from dataclasses import dataclass, field
from typing import List, Optional, Union
from cdabindings.org.hl7.v3.ad import Ad
from cdabindings.org.hl7.v3.cr import CE
from cdabindings.org.hl7.v3.cs import CS
from cdabindings.org.hl7.v3.entity_class_organization import EntityClassOrganization
from cdabindings.org.hl7.v3.entity_determiner import EntityDeterminer
from cdabindings.org.hl7.v3.ii import II
from cdabindings.org.hl7.v3.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.org.hl7.v3.ivl_ts import IvlTs
from cdabindings.org.hl7.v3.null_flavor import NullFlavor
from cdabindings.org.hl7.v3.on import On
from cdabindings.org.hl7.v3.role_class_mutual_relationship import RoleClassMutualRelationship
from cdabindings.org.hl7.v3.role_class_ontological import RoleClassOntological
from cdabindings.org.hl7.v3.role_class_partitive import RoleClassPartitive
from cdabindings.org.hl7.v3.role_class_passive import RoleClassPassive
from cdabindings.org.hl7.v3.role_class_root_value import RoleClassRootValue
from cdabindings.org.hl7.v3.tel import Tel
from cdabindings.org.hl7.v3.x_document_entry_subject import XDocumentEntrySubject
from cdabindings.org.hl7.v3.x_document_subject import XDocumentSubject
from cdabindings.org.hl7.v3.x_information_recipient_role import XInformationRecipientRole
from cdabindings.org.hl7.v3.x_role_class_accommodation_requestor import XRoleClassAccommodationRequestor
from cdabindings.org.hl7.v3.x_role_class_coverage import XRoleClassCoverage
from cdabindings.org.hl7.v3.x_role_class_coverage_invoice import XRoleClassCoverageInvoice
from cdabindings.org.hl7.v3.x_role_class_credentialed_entity import XRoleClassCredentialedEntity
from cdabindings.org.hl7.v3.x_role_class_payee_policy_relationship import XRoleClassPayeePolicyRelationship

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class OrganizationPartOf:
    class Meta:
        name = "POCD_MT000040.OrganizationPartOf"

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
    id: List[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[CE] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    whole_organization: Optional["Organization"] = field(
        default=None,
        metadata={
            "name": "wholeOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Union[str, RoleClassMutualRelationship, RoleClassPassive, RoleClassOntological, RoleClassPartitive, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship, RoleClassRootValue] = field(
        init=False,
        default=RoleClassPartitive.PART,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class Organization:
    class Meta:
        name = "POCD_MT000040.Organization"

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
    id: List[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    name: List[On] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    telecom: List[Tel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    addr: List[Ad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    standard_industry_class_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "standardIndustryClassCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    as_organization_part_of: Optional[OrganizationPartOf] = field(
        default=None,
        metadata={
            "name": "asOrganizationPartOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: EntityClassOrganization = field(
        init=False,
        default=EntityClassOrganization.ORG,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )
