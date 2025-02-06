import socket
import threading

# Настраиваем параметры подключения
SERVER_IP = "127.0.0.1"  # IP-адрес сервера
SERVER_PORT = 12345      # Порт сервера

# Функция для чтения сообщений от сервера
def receive_messages(client_socket):
    while True:
        try:
            # Получаем сообщение от сервера
            message = client_socket.recv(1024).decode()
            if not message:
                print("Соединение с сервером разорвано.")
                break
            print(f"Сервер: {message}")
        except:
            print("Ошибка при получении сообщения.")
            break

# Создаем клиентский сокет
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Подключаемся к серверу
    client.connect((SERVER_IP, SERVER_PORT))
    print("Подключено к серверу!")
except:
    print("Не удалось подключиться к серверу.")
    exit()

# Запускаем поток для чтения сообщений от сервера
thread = threading.Thread(target=receive_messages, args=(client,))
thread.daemon = True  # Поток завершится, когда завершится программа
thread.start()

# Основной цикл для отправки сообщений
print("Введите сообщения (или 'exit' для выхода):")
while True:
    message = input()
    if message.lower() == "exit":
        print("Отключение от сервера...")
        client.close()
        break
    try:
        # Отправляем сообщение на сервер
        client.send(message.encode())
    except:
        print("Ошибка при отправке сообщения. Соединение закрыто.")
        break
