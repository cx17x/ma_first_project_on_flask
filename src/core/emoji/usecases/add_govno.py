import dataclasses

from src.core.emoji.entites import Emoji
from src.core.emoji.repo.i_emoji_repo import IEmojiRepo
from src.core.usecase import IUseCase


@dataclasses.dataclass
class AddNewEmojiDTO:
    emoji: Emoji


class AddNewEmojiUC(IUseCase):
    def __init__(self, emoji_repo: IEmojiRepo):
        self.emoji_repo = emoji_repo

    def execute(self, dto: AddNewEmojiDTO) -> Emoji:
        new_emoji = self.emoji_repo.add_new_emoji(dto.emoji)
        return new_emoji
