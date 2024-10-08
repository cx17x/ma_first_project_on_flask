from abc import ABC, abstractmethod

from src.core.emoji.entites import Emoji


class IEmojiRepo(ABC):
    @abstractmethod
    def get_by_id(self, emoji_id: int) -> Emoji:
        pass

    @abstractmethod
    def get_random_emoji(self) -> Emoji:
        pass

    @abstractmethod
    def update_by_id(self, emoji_id: int, emoji: Emoji) -> Emoji:
        pass

    @abstractmethod
    def add_new_emoji(self, emoji: Emoji) -> Emoji:
        pass

    @abstractmethod
    def delete_emoji(self, emoji_id: int) -> None:
        pass
