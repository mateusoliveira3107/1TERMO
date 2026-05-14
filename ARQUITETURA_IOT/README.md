# 🌐 Arquitetura de IoT (Internet das Coisas)

## 📌 Conteúdo de Sala de Aula

### 1. Fundamentos de IoT
* **Arquitetura em Camadas:** Percepção (sensores), Rede (transmissão) e Aplicação (nuvem).
* **Protocolos de Comunicação:** MQTT, HTTP, CoAP e LoRaWAN.
* **Edge vs. Cloud Computing:** Processamento local contra processamento na nuvem.

### 2. Hardware e Sensores
* **Sensores:** Coleta de dados físicos (temperatura, umidade, presença).
* **Atuadores:** Execução de ações físicas (motores, relés, LEDs).
* **Sinais:** Diferenças práticas entre inputs/outputs Analógicos e Digitais.

---

## 🤖 Ecossistema Arduino

### 1. Visão Geral da Plataforma
* **Prototipagem Rápida:** Placa de desenvolvimento de hardware livre.
* **Microcontrolador:** Geralmente ATmega328P (no modelo Arduino Uno).
* **Ambiente IDE:** Software para escrita, compilação e upload do código.

### 2. Pinagem e Conexões (Pinout)
* **Pinos Digitais:** Operam em níveis lógicos altos (5V/3.3V) ou baixos (0V).
* **Pinos Analógicos:** Leitura de tensões variáveis via conversor ADC.
* **PWM (Pulse Width Modulation):** Simulação de saídas analógicas nos pinos digitais.

---

## 💻 Linguagens de Programação em IoT

### 1. Linguagem C++ (Foco em Hardware/Edge)
* **Uso:** Utilizada diretamente na IDE do Arduino para controle de baixo nível.
* **Estrutura Base:**
  * `setup()`: Roda uma vez ao iniciar a placa para configurações.
  * `loop()`: Executa continuamente o código principal.
* **Exemplo de Código (Piscar LED):**

```cpp
const int LED_PIN = 13;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH);
  delay(1000);
  digitalWrite(LED_PIN, LOW);
  delay(1000);
}
```

### 2. Linguagem Python (Foco em Gateways e Nuvem)
* **Uso:** Processamento de dados, comunicação com bancos de dados e dashboards.
* **MicroPython:** Versão otimizada para microcontroladores avançados (ESP32, Raspberry Pi Pico).
* **Exemplo de Código (Leitura Serial do Arduino via PC):**

```python
import serial
import time

# Configura a porta serial (ajuste a porta conforme seu sistema)
porta = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

while True:
    if porta.in_waiting > 0:
        dados = porta.readline().decode('utf-8').rstrip()
        print(f"Dados do Sensor: {dados}")
    time.sleep(0.5)
```

---

## 🛠️ Projetos Práticos Sugeridos
1. **Semáforo Inteligente:** Lógica de temporização em C++.
2. **Monitor de Clima Local:** Sensor DHT11 com envio de alertas.
3. **Dashboard IoT:** Python lendo dados do Arduino e exibindo gráficos em tempo real.