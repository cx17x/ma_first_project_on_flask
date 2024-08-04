from dataclasses import asdict

from flask import Blueprint, jsonify

from src.core.emoji.usecases.get_random_govno import GetRandomGovnoUC, GetRendomGonvoDTO
from src.data.emoji.repo.emoji_repo_list import EmojiRepoList

emoji_bp = Blueprint('emoji', __name__)
@emoji_bp.route('/govno', methods=['GET'])
def get_random_govno():
    usecase = GetRandomGovnoUC(EmojiRepoList())
    dto = GetRendomGonvoDTO()
    result = usecase.execute(dto=dto)
    return jsonify(asdict(result))

