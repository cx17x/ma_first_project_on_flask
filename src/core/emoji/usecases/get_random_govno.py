import dataclasses

from src.core.emoji.entites import Emoji
from src.core.emoji.repo.i_emoji_repo import IEmojiRepo
from src.core.usecase import IUseCase


@dataclasses.dataclass
class GetRendomGonvoDTO:
    pass


class GetRandomGovnoUC(IUseCase):
    def __init__(self, emoji_repo: IEmojiRepo):
        self.emoji_repo = emoji_repo
    def execute(self, dto: GetRendomGonvoDTO) -> Emoji:
        return self.emoji_repo.get_random_emoji()
