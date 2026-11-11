import sys
import websocket

proyecto, token = sys.argv[1], sys.argv[2]
ws = websocket.create_connection(f"ws://127.0.0.1:8000/ws/projects/{proyecto}/?token={token}")
print("Conectado. Esperando mensajes (Ctrl+C para salir)...")
while True:
    print(ws.recv())
