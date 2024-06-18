from dataclasses import dataclass

from cdabindings.in_fulfillment_of1_1 import InFulfillmentOf11

__NAMESPACE__ = "urn:hl7-org:sdtc"


@dataclass
class InFulfillmentOf1(InFulfillmentOf11):
    class Meta:
        name = "inFulfillmentOf1"
        namespace = "urn:hl7-org:sdtc"
