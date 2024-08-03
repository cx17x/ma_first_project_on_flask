# Короче на фласк/фастапи(в синхронном режиме)
# Хранить все в обычном списке
# 4 метода
# /govno GET
# Отдает случайный эмодзи какашки строкой. Чтобы было как минимум 3 варианта по умолчанию
# /govno/<id> GET
# Из ссылки забрать id, отдать какашку с соотвествующим порядковым номером. Если такого id нет(вышел за пределы) - отдать 404 код
# /govno/<id> PUT
# Заменяет эмодзи какашки с переданным порядковым номером на присланное. Если id вышел  за границы - 404. Проверить что заслали именно эмодзи, если нет - 400 ошибка отдается
# /govno POST
# Принимает эмодзи и кладет его в список. Если такой уже есть - отдает 409 код ошибки

# 🐯 🐰 🐱 🐲 🐳 🐴 🐵 🐶 🐷
import random
from flask import Flask, jsonify, request
from emoji import is_emoji

app = Flask(__name__)

govno_emojis = ['💩', '🤢', '🤮']


@app.route('/govno', methods=['GET'])
def get_random_govno():
    return jsonify(random.choice(govno_emojis))


@app.route('/govno/<int:id>', methods=['GET'])
def get_govno_by_id(id):
    if id < 0 or id >= len(govno_emojis):
        return jsonify({'error': 'Not found'}, 404)
    return jsonify(govno_emojis[id])


@app.route('/govno/<int:id>', methods=['PUT'])
def update_govno_by_id(id:int):
    if id < 0 or id >= len(govno_emojis):
        return jsonify({'error': 'Not found'}), 404
    new_emoji = request.json.get('emoji')
    if not new_emoji or len(new_emoji) != 1:
        return jsonify({'error': 'Bad request'}), 400
    govno_emojis[id] = new_emoji
    return jsonify(govno_emojis[id])


@app.route('/govno', methods=['POST'])
def add_govno():
    new_emoji = request.json.get('emoji')
    if not new_emoji or len(new_emoji) != 1:
        return jsonify({'error': 'Bad request'}), 400
    if not is_emoji(new_emoji):
        return jsonify({'error': 'Not emoji'}), 400
    if new_emoji in govno_emojis:
        return jsonify({'error': 'Dublicate'}), 409
    govno_emojis.append(new_emoji)
    return jsonify(new_emoji), 201

@app.route('/govno/<int:id>', methods=['DELETE'])
def delete(id):
    if id < 0 or id >= len(govno_emojis):
        return jsonify({'error': 'Not found'}), 404
    deleted_emoji = govno_emojis.pop(id)
    return jsonify({'message': 'Emoji deleted', 'deleted_emoji': deleted_emoji}),200

if __name__ == '__main__':
    app.run(debug=True)
