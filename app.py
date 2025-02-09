from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Для работы с запросами с фронтенда

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Используем SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)  # Разрешаем CORS для взаимодействия с фронтендом


# Определение модели сообщений
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)


# Создаем таблицы в базе данных в контексте приложения
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


# API для отправки сообщений
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json  # Получаем JSON-данные от клиента
    message_text = data.get("message")  # Извлекаем сообщение

    if not message_text:
        return jsonify({"error": "Сообщение не может быть пустым"}), 400

    new_message = Message(text=message_text)
    db.session.add(new_message)
    db.session.commit()

    return jsonify({"status": "success", "message": message_text})


if __name__ == '__main__':

    app.run(debug=True)
