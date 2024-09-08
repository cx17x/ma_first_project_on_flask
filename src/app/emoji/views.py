from dataclasses import asdict

from flask import Blueprint, jsonify, request

from src.core.emoji.usecases.add_govno import AddNewEmojiUC, AddNewEmojiDTO
from src.core.emoji.usecases.delete_emoji import DeleteEmojiUC, DeleteEmojiDTO
from src.core.emoji.usecases.get_govno_by_id import GetGovnoByIdUC, GetGovnoByIdDTO
from src.core.emoji.usecases.get_random_govno import GetRandomGovnoUC, GetRendomGonvoDTO
from src.core.emoji.usecases.update_by_id import UpdateByIdDTO, UpdateByIdUC
from src.data.database import new_session
from src.data.emoji.repo.sqlA_emoji_repo import EmojiRepoDB

emoji_bp = Blueprint('emoji', __name__)
@emoji_bp.route('/govno', methods=['GET'])
def get_random_govno():
    usecase = GetRandomGovnoUC(emoji_repo=EmojiRepoDB(new_session()))
    dto = GetRendomGonvoDTO()
    result = usecase.execute(dto=dto)
    return jsonify(asdict(result))

@emoji_bp.route('/govno/<int:id>', methods=['GET'])
def get_govno_by_id(id: int):
    usercase = GetGovnoByIdUC(emoji_repo=EmojiRepoDB(new_session()))
    dto = GetGovnoByIdDTO(id=id)
    result = usercase.execute(dto=dto)
    return jsonify(asdict(result))

@emoji_bp.route('/govno/<int:id>', methods=['PUT'])
def update_by_id(id):
    usercase = UpdateByIdUC(emoji_repo=EmojiRepoDB(new_session()))
    data = request.json
    print(data)
    dto = UpdateByIdDTO(id=id, str_emoji=data.get('emoji'))
    result = usercase.execute(dto=dto)
    return jsonify(asdict(result))

@emoji_bp.route('/govno/<int:id>', methods=['DELETE'])
def delete_emoji(id):
    usercase = DeleteEmojiUC(emoji_repo=EmojiRepoDB(new_session()))
    # data = request.json
    dto = DeleteEmojiDTO(emoji_id=id)
    result = usercase.execute(dto=dto)
    return jsonify(asdict(result))

@emoji_bp.route('/govno', methods=['POST'])
def add_emoji():
    usercase = AddNewEmojiUC(emoji_repo=EmojiRepoDB(new_session()))
    dto = AddNewEmojiDTO()
    result = usercase.execute(dto=dto)
    return jsonify(asdict(result))
