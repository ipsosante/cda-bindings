from dataclasses import dataclass, field
from typing import Optional

from cdabindings.pq import Pq
from cdabindings.probability_distribution_type import (
    ProbabilityDistributionType,
)
from cdabindings.ts import TS

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class PpdTs(TS):
    """
    :ivar standard_deviation: The primary measure of
        variance/uncertainty of the value (the square root of the sum of
        the squares of the differences between all data points and the
        mean). The standard deviation is used to normalize the data for
        computing the distribution function. Applications that cannot
        deal with probability distributions can still get an idea about
        the confidence level by looking at the standard deviation.
    :ivar distribution_type: A code specifying the type of probability
        distribution. Possible values are as shown in the attached
        table. The NULL value (unknown) for the type code indicates that
        the probability distribution type is unknown. In that case, the
        standard deviation has the meaning of an informal guess.
    """

    class Meta:
        name = "PPD_TS"

    standard_deviation: Optional[Pq] = field(
        default=None,
        metadata={
            "name": "standardDeviation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    distribution_type: Optional[ProbabilityDistributionType] = field(
        default=None,
        metadata={
            "name": "distributionType",
            "type": "Attribute",
        },
    )
