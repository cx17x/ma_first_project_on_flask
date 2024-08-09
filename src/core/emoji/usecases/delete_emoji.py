import dataclasses

from src.core.emoji.entites import Emoji
from src.core.emoji.repo.i_emoji_repo import IEmojiRepo
from src.core.usecase import IUseCase


@dataclasses.dataclass
class DeleteEmojiDTO:
    emoji_id: int


class DeleteEmojiUC(IUseCase):
    def __init__(self, emoji_repo: IEmojiRepo):
        self.emoji_repo = emoji_repo

    def execute(self, dto: DeleteEmojiDTO) -> Emoji:
        delete_emoji = self.emoji_repo.delete_emoji(dto.emoji_id)
        return delete_emoji
