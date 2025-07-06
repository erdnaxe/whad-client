from dataclasses import dataclass, field
from typing import Optional

@dataclass
class InjectionConfiguration:
    """
    Configuration for injecting into ZigBee communication.

    :param channel: select the channel to use for injection (c)

    """
    channel : Optional[int] = None
