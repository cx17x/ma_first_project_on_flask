import dataclasses

from src.core.emoji.entites import Emoji
from src.core.emoji.repo.i_emoji_repo import IEmojiRepo
from src.core.usecase import IUseCase


@dataclasses.dataclass
class GetGovnoByIdDTO:
    id: int


class GetGovnoByIdUC(IUseCase):
    def __init__(self, emoji_repo: IEmojiRepo):
        self.emoji_repo = emoji_repo

    def execute(self, dto: GetGovnoByIdDTO) -> Emoji:
        return self.emoji_repo.get_by_id(emoji_id=dto.id)
