from sqlalchemy import Column, Integer, String, MetaData

from src.data.database import Base

metadata_obj = MetaData()

class EmojiModel(Base):
    __tablename__ = 'emojis'

    id = Column(Integer, primary_key=True, index=True)
    emoji = Column(String, index=True)

    # id: Mapped[int] = mapped_column(primary_key=True)
    # emoji: Mapped[str]
