import socket
from _thread import start_new_thread

# Настраиваем сервер
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 12345))  # IP и порт
server.listen(5)

print("Сервер запущен и прослушивает соединения...")

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Сообщение от клиента: {message}")
            # Отправляем ответ
            client_socket.send("Сообщение получено".encode())
        except:
            break
    client_socket.close()

# Основной цикл прослушивания соединений
while True:
    client_socket, client_address = server.accept()
    print(f"Подключился клиент: {client_address}")
    start_new_thread(handle_client, (client_socket,))

