import random

from sqlalchemy.orm import Session
from src.core.emoji.entites import Emoji
from src.core.emoji.repo.exeptions import NotFound, Dublicate
from src.core.emoji.repo.i_emoji_repo import IEmojiRepo
from src.data.database import new_session

from src.data.emoji.model import EmojiModel


class EmojiRepoDB(IEmojiRepo):
    def _model_to_entyty(self, model: EmojiModel) -> Emoji:
        return Emoji(
            id=model.id,
            emoji=model.emoji
        )

    def _entyty_to_model(self, emoji: Emoji) -> EmojiModel:
        return EmojiModel(
            id=emoji.id,
            emoji=emoji.emoji
        )

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_random_emoji(self) -> Emoji:
        emoji = self.db.query(EmojiModel).all()
        res = random.choice(emoji)
        return self._model_to_entyty(res)

    def get_by_id(self, emoji_id: int) -> Emoji:
        emoji_out = self.db.query(EmojiModel).filter(EmojiModel.id == emoji_id).first()
        if emoji_out is None:
            raise NotFound
        return self._model_to_entyty(emoji_out)

    def update_by_id(self, emoji_id: int, emoji: Emoji) -> Emoji:
        new_emoji = self.db.query(EmojiModel).filter(EmojiModel.id == emoji_id).first()
        if new_emoji is None:
            raise NotFound(f'Emoji with id {emoji_id} not found')
        new_emoji.emoji = emoji.emoji
        self.db.commit()
        self.db.refresh(new_emoji)

        return self._model_to_entyty(new_emoji)

    def delete_emoji(self, emoji_id: int) -> None:
        emoji = self.db.query(EmojiModel).filter(EmojiModel.id == emoji_id).first()
        self.db.delete(emoji)
        self.db.commit()

    def add_new_emoji(self, emoji: Emoji) -> Emoji:
        db_emoji = self.db.query(EmojiModel).filter(EmojiModel.id == emoji.id).first()
        if db_emoji:
            raise Dublicate
        db_emoji = EmojiModel(id=emoji.id, emoji=emoji.emoji)
        self.db.add(db_emoji)
        self.db.commit()
        self.db.refresh(db_emoji)
        return self._model_to_entyty(db_emoji)


# repo = EmojiRepoDB(new_session())
# emoji = repo.update_by_id(emoji_id=3, emoji=Emoji(id=3, emoji='🚀'))
# emoji_entyty = repo._model_to_entyty(emoji)
# print(emoji_entyty)
# repo = new_session()
# ✅ ✔️ ❌ 👌 ❎ ❔ ☑️ 🗳️ ❕ 🔘 🙆
# emoji1 = EmojiModel(id=1, emoji="😊")
# emoji2 = EmojiModel(id=2, emoji="🚀")
# emoji3 = EmojiModel(id=3, emoji="🐶")
#
# repo.add_all([emoji1, emoji2, emoji3])
# repo.commit()
#
# emojis = repo.query(EmojiModel).all()
#
# for emoji in emojis:
#     print(emoji.emoji)
#
# repo.close()
