import network
import socket
import dht
from machine import Pin
from time import sleep

# ===== WIFI =====
SSID = "OLIMPIADA"
SENHA = "#09#17#58"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, SENHA)

print("Conectando ao Wi-Fi...")

while not wifi.isconnected():
    sleep(1)

print("Conectado!")
print("IP do ESP32:", wifi.ifconfig()[0])

# ===== SENSOR =====
sensor = dht.DHT11(Pin(4))

# ===== SERVIDOR WEB =====
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(1)

print("Servidor iniciado")

while True:

    client, endereco = server.accept()
    print("Cliente conectado:", endereco)

    request = client.recv(1024)

    # Lê sensor
    sensor.measure()

    temperatura = sensor.temperature()
    umidade = sensor.humidity()

    # Página HTML
    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="2">
        <title>ESP32 DHT11</title>
    </head>

    <body style="font-family:Arial; text-align:center; margin-top:50px;">
        <h1>ESP32 + DHT11</h1>

        <h2>🌡 Temperatura</h2>
        <p style="font-size:40px;">{temperatura} °C</p>

        <h2>💧 Umidade</h2>
        <p style="font-size:40px;">{umidade} %</p>
    </body>
    </html>
    """

    client.send("HTTP/1.1 200 OK\r\n")
    client.send("Content-Type: text/html\r\n")
    client.send("Connection: close\r\n\r\n")
    client.sendall(html)

    client.close()
