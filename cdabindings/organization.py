from dataclasses import dataclass, field
from typing import Optional

from cdabindings.ad import Ad
from cdabindings.ce import CE
from cdabindings.cs import CS
from cdabindings.entity_class_organization import EntityClassOrganization
from cdabindings.entity_determiner import EntityDeterminer
from cdabindings.ii import II
from cdabindings.infrastructure_root_type_id import InfrastructureRootTypeId
from cdabindings.ivl_ts import IvlTs
from cdabindings.null_flavor import NullFlavor
from cdabindings.on import On
from cdabindings.role_class import RoleClass
from cdabindings.tel import Tel

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Organization:
    class Meta:
        name = "POCD_MT000040.Organization"

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
    id: list[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    name: list[On] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    telecom: list[Tel] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    addr: list[Ad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    standard_industry_class_code: Optional[CE] = field(
        default=None,
        metadata={
            "name": "standardIndustryClassCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    as_organization_part_of: Optional["OrganizationPartOf"] = field(
        default=None,
        metadata={
            "name": "asOrganizationPartOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClassOrganization = field(
        init=False,
        default=EntityClassOrganization.ORG,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        },
    )


@dataclass
class OrganizationPartOf:
    class Meta:
        name = "POCD_MT000040.OrganizationPartOf"

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
    id: list[II] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: Optional[CE] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    status_code: Optional[CS] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    whole_organization: Optional[Organization] = field(
        default=None,
        metadata={
            "name": "wholeOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClass = field(
        init=False,
        default=RoleClass.PART,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
