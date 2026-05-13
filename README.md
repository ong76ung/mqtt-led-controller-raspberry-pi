# Implementing a Device Control System Using MQTT Communication with Raspberry Pi

라즈베리파이와 MQTT 통신을 활용하여 PC에서 LED 3개를 제어하는 IoT 프로젝트입니다.

## 🎬 데모 영상

[![Demo Video](https://img.youtube.com/vi/1y882kDPPxY/0.jpg)](https://www.youtube.com/watch?v=1y882kDPPxY)

## 📌 프로젝트 개요

- PC의 MQTT.fx에서 발행한 메시지를 라즈베리파이가 구독하여 LED 제어
- threading 기법을 활용한 단방향 및 양방향 MQTT 통신 구현
- 초록·파랑·빨강 LED 3개를 GPIO 핀으로 제어

## 🛠️ 사용 기술

| 항목 | 내용 |
|---|---|
| Language | Python 3.x |
| Protocol | MQTT |
| Library | paho-mqtt, gpiozero, threading |
| Tool | MQTT.fx |
| Hardware | Raspberry Pi, LED x3, 330옴 저항 x3 |

## 📂 파일 구성

```
project_30/
├── main30.py        # 단방향 MQTT 통신 LED 제어
└── main30-1.py      # 양방향 MQTT 통신 LED 제어 (threading)
```

## 🚀 실행 방법

```bash
# 가상환경 활성화
source {가상환경이름}/bin/activate

# 단방향 통신 실행
python3 main30.py

# 양방향 통신 실행
python3 main30-1.py
```

## ⚙️ 사전 준비

```bash
# 라이브러리 설치 순서
sudo apt install swig
sudo apt install liblgpio-dev
pip install lgpio
pip install gpiozero
```

- MQTT.fx 설치 및 브로커 IP 주소 확인 필요
- `broker_address` 에 본인 라즈베리파이 IP 주소 입력 필요

## 📚 참고문헌

- [MQTT Protocol Documentation](https://mqtt.org/)
- [paho-mqtt Python Client Documentation](https://eclipse.dev/paho/files/paho.mqtt.python/html/index.html)
- [threading - Thread-based parallelism](https://docs.python.org/3/library/threading.html)
- [GPIO Zero Documentation](https://gpiozero.readthedocs.io/)
