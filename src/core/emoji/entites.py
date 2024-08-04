import dataclasses
from typing import Optional


@dataclasses.dataclass
class Emoji:
    emoji: str
    id: Optional[int] = None

