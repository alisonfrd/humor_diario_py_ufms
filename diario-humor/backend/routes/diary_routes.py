from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models.diary import DiaryEntry
from datetime import datetime

diary_bp = Blueprint('diary', __name__, url_prefix='/diary')

# 1. Criar uma nova entrada
@diary_bp.route('/', methods=['POST'])
@jwt_required()
def create_entry():
    data = request.get_json()
    text = data.get('text')
    mood = data.get('mood')
    entry_date_str = data.get('entry_date')  # string tipo "2024-06-10"
    user_id = get_jwt_identity()

    if not text or not mood or not entry_date_str:
        return jsonify({'error': 'Texto, humor e data são obrigatórios.'}), 400

    try:
        entry_date = datetime.strptime(entry_date_str, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({'error': 'Formato de data inválido. Use YYYY-MM-DD.'}), 400

    # Não permitir mais de uma entrada por usuário na mesma data
    existing = DiaryEntry.query.filter_by(user_id=user_id, entry_date=entry_date).first()
    if existing:
        return jsonify({'error': 'Já existe entrada para essa data. Use editar.'}), 409

    entry = DiaryEntry(text=text, mood=mood, entry_date=entry_date, user_id=user_id)
    db.session.add(entry)
    db.session.commit()
    return jsonify({'message': 'Entrada criada com sucesso.'}), 201

# 2. Listar entradas do usuário
@diary_bp.route('/', methods=['GET'])
@jwt_required()
def list_entries():
    user_id = get_jwt_identity()
    entries = DiaryEntry.query.filter_by(user_id=user_id).order_by(DiaryEntry.entry_date.desc()).all()

    result = []
    for entry in entries:
        result.append({
            'id': entry.id,
            'text': entry.text,
            'mood': entry.mood,
            'entry_date': entry.entry_date.isoformat(),
            'created_at': entry.created_at.isoformat()
        })
    return jsonify(result), 200

# 3. Editar entrada existente (por id)
@diary_bp.route('/<int:entry_id>', methods=['PUT'])
@jwt_required()
def update_entry(entry_id):
    user_id = get_jwt_identity()
    entry = DiaryEntry.query.filter_by(id=entry_id, user_id=user_id).first()
    if not entry:
        return jsonify({'error': 'Entrada não encontrada.'}), 404

    data = request.get_json()
    text = data.get('text')
    mood = data.get('mood')
    entry_date_str = data.get('entry_date')

    if entry_date_str:
        try:
            entry_date = datetime.strptime(entry_date_str, "%Y-%m-%d").date()
            # Não permitir duplicidade se mudar a data
            duplicate = DiaryEntry.query.filter_by(user_id=user_id, entry_date=entry_date).first()
            if duplicate and duplicate.id != entry.id:
                return jsonify({'error': 'Já existe entrada para essa data.'}), 409
            entry.entry_date = entry_date
        except ValueError:
            return jsonify({'error': 'Formato de data inválido. Use YYYY-MM-DD.'}), 400

    if text:
        entry.text = text
    if mood:
        entry.mood = mood

    db.session.commit()
    return jsonify({'message': 'Entrada atualizada com sucesso.'}), 200

# 4. Excluir entrada (por id)
@diary_bp.route('/<int:entry_id>', methods=['DELETE'])
@jwt_required()
def delete_entry(entry_id):
    user_id = get_jwt_identity()
    entry = DiaryEntry.query.filter_by(id=entry_id, user_id=user_id).first()
    if not entry:
        return jsonify({'error': 'Entrada não encontrada.'}), 404

    db.session.delete(entry)
    db.session.commit()
    return jsonify({'message': 'Entrada excluída com sucesso.'}), 200
