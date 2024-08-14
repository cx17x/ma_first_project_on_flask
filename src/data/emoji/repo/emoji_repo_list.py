from src.core.emoji.entites import Emoji
from src.core.emoji.repo.exeptions import NotFound
from src.core.emoji.repo.i_emoji_repo import IEmojiRepo
import random


class EmojiRepoList(IEmojiRepo):
    my_list = {1: Emoji(emoji='🐷', id=1), 2: Emoji(emoji='🐰', id=2), 3: Emoji(emoji='🐵', id=3)}  # key:id, value: emoji

    def get_by_id(self, emoji_id: int) -> Emoji:
        emoji = self.my_list.get(emoji_id)
        if emoji is None:
            raise NotFound
        else:
            return emoji

    def get_random_emoji(self) -> Emoji:
        emoji = self.my_list[random.choice(list(self.my_list.keys()))]
        return emoji

    def update_by_id(self, emoji_id: int, emoji: Emoji) -> Emoji:
        if emoji_id not in self.my_list:
            raise NotFound
        self.my_list[emoji_id] = emoji
        return self.my_list[emoji_id]

    def delete_emoji(self, emoji_id: int) -> Emoji:
        if emoji_id not in self.my_list:
            raise NotFound
        deleted_emoji = self.my_list.pop(emoji_id)
        return deleted_emoji

    def add_emoji(self, emoji_id: int, emoji: Emoji) -> Emoji:
        if emoji_id in self.my_list:
            raise Dublicate
        self.my_list[emoji_id] = emoji
        return emoji
