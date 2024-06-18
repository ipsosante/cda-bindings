from dataclasses import dataclass

from cdabindings.order_1 import Order1

__NAMESPACE__ = "urn:dicom-org:ps3-20"


@dataclass
class Order(Order1):
    class Meta:
        name = "order"
        namespace = "urn:dicom-org:ps3-20"
