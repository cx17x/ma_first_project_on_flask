import random

from sqlalchemy.orm import Session

from src.core.emoji.entites import Emoji
from src.core.emoji.repo.exeptions import NotFound, Dublicate
from src.core.emoji.repo.i_emoji_repo import IEmojiRepo
from src.data.database import new_session

from src.data.emoji.model import EmojiModel


class EmojiRepoDB(IEmojiRepo):
    def _entyty_to_model(self, emoji: Emoji) -> EmojiModel:
        return EmojiModel(
            id=emoji.id,
            emoji=emoji.emoji
        )

    def _model_to_entyty(self, emoji: EmojiModel) -> Emoji:
        return Emoji(
            id=emoji.id,
            emoji=emoji.emoji
        )

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_by_id(self, emoji_id: int) -> Emoji:
        emoji = self.db.query(EmojiModel).filter(id=emoji_id).first()
        if emoji is None:
            raise NotFound
        return self._model_to_entyty(emoji)

    def get_random_emoji(self) -> Emoji:
        emoji = self.db.query(EmojiModel).all()
        res = random.choice(emoji)
        return self._model_to_entyty(res)
    def update_by_id(self, emoji_id: int, emoji: Emoji) -> Emoji:
        pass

    def delete_emoji(self, emoji_id: int) -> Emoji:
        db_emoji = self.get_random_emoji(emoji_id)
        self.db.delete(db_emoji)
        self.db.commit()
        return db_emoji

    def add_new_emoji(self, emoji: Emoji) -> Emoji:
        db_emoji = self.db.query(EmojiModel).filter(Emoji.id == emoji.id).first()
        if db_emoji:
            raise Dublicate
        db_emoji = Emoji(id=emoji.id, emoji=emoji.emoji)
        self.db.add(db_emoji)
        self.db.commit()
        self.db.refresh(db_emoji)
        return self._model_to_entyty(db_emoji)



