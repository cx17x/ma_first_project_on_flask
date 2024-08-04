import dataclasses

from src.core.emoji.entites import Emoji
from src.core.emoji.repo.i_emoji_repo import IEmojiRepo
from src.core.usecase import IUseCase


@dataclasses.dataclass
class UpdateByIdDTO:
    str_emoji: str
    id: int


class UpdateByIdUC(IUseCase):
    def __init__(self, emoji_repo: IEmojiRepo):
        self.emoji_repo = emoji_repo

    def execute(self, dto: UpdateByIdDTO) -> Emoji:
        return self.emoji_repo.update_by_id(emoji=Emoji(emoji=dto.str_emoji), emoji_id=dto.id)
