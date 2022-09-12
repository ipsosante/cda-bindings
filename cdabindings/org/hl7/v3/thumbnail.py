from dataclasses import dataclass
from cdabindings.org.hl7.v3.ed import ED

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class Thumbnail(ED):
    """A thumbnail is an abbreviated rendition of the full data.

    A thumbnail requires significantly fewer resources than the full
    data, while still maintaining some distinctive similarity with the
    full data. A thumbnail is typically used with by-reference
    encapsulated data. It allows a user to select data more efficiently
    before actually downloading through the reference.
    """
    class Meta:
        name = "thumbnail"
