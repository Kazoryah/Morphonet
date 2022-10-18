"""One layer network with PConv function."""

from typing import Union, Tuple, Callable, Any
import torch

from .base import BaseNetwork
from .layers.scale_bias import ScaleBias
from .layers.pconv import PConv


class PConvNet(BaseNetwork):
    """Network with one PConv layer."""

    def __init__(
        self,
        filter_size: Union[int, Tuple[int, int]],
        loss_function: Callable,
        **kwargs: Any,
    ):
        super().__init__(loss_function=loss_function)
        self.pconv1 = PConv(
            in_channels=1, out_channels=1, filter_size=filter_size, **kwargs
        )
        self.sb1 = ScaleBias(num_features=1, **kwargs)

    def forward(
        self, batch: torch.Tensor, *args: Any, **kwargs: Any
    ) -> torch.Tensor:
        # pylint: disable=arguments-differ
        batch = self.pconv1(batch)
        batch = self.sb1(batch)

        return batch
