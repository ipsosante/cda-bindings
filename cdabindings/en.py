from dataclasses import dataclass, field

from cdabindings.any_abstract import AnyAbstract
from cdabindings.en_delimiter import EnDelimiter
from cdabindings.en_family import EnFamily
from cdabindings.en_given import EnGiven
from cdabindings.en_prefix import EnPrefix
from cdabindings.en_suffix import EnSuffix
from cdabindings.entity_name_use import EntityNameUse
from cdabindings.ivl_ts import IvlTs

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class En(AnyAbstract):
    """A name for a person, organization, place or thing.

    A sequence of name parts, such as given name or family name, prefix,
    suffix, etc. Examples for entity name values are "Jim Bob Walton,
    Jr.", "Health Level Seven, Inc.", "Lake Tahoe", etc. An entity name
    may be as simple as a character string or may consist of several
    entity name parts, such as, "Jim", "Bob", "Walton", and "Jr.",
    "Health Level Seven" and "Inc.", "Lake" and "Tahoe".

    :ivar use: A set of codes advising a system or user which name in a
        set of like names to select for a given purpose. A name without
        specific use code might be a default name useful for any
        purpose, but a name with a specific use code would be preferred
        for that respective purpose.
    :ivar content:
    """

    class Meta:
        name = "EN"

    use: list[EntityNameUse] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "delimiter",
                    "type": EnDelimiter,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "family",
                    "type": EnFamily,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "given",
                    "type": EnGiven,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "prefix",
                    "type": EnPrefix,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "suffix",
                    "type": EnSuffix,
                    "namespace": "urn:hl7-org:v3",
                },
                {
                    "name": "validTime",
                    "type": IvlTs,
                    "namespace": "urn:hl7-org:v3",
                },
            ),
        },
    )
