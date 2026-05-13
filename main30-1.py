import paho.mqtt.client as mqtt          # MQTT 통신 모듈 불러오기
import time                              # 시간 관련 기능 모듈 불러오기
from gpiozero import LED                 # GPIO 제어 모듈에서 LED 클래스 불러오기
import threading                         # 두 작업을 동시에 처리하기 위한 스레드 모듈 불러오기

greenLed = LED(16)                       # 16번 GPIO 핀에 연결된 초록 LED 설정
blueLed  = LED(20)                       # 20번 GPIO 핀에 연결된 파란 LED 설정
redLed   = LED(21)                       # 21번 GPIO 핀에 연결된 빨간 LED 설정

def on_message(client, userdata, msg):   # 메시지 수신 시 자동으로 실행되는 콜백 함수
    print(msg.topic + " " + str(msg.payload))  # 수신된 토픽과 바이트 데이터 출력
    message = msg.payload.decode()       # 바이트 데이터를 문자열로 변환
    print(message)                       # 변환된 메시지 출력

    if message == "green_on":            # 메시지가 "green_on"이면
        greenLed.on()                    # 초록 LED 켜기
    elif message == "green_off":         # 메시지가 "green_off"이면
        greenLed.off()                   # 초록 LED 끄기
    elif message == "blue_on":           # 메시지가 "blue_on"이면
        blueLed.on()                     # 파란 LED 켜기
    elif message == "blue_off":          # 메시지가 "blue_off"이면
        blueLed.off()                    # 파란 LED 끄기
    elif message == "red_on":            # 메시지가 "red_on"이면
        redLed.on()                      # 빨간 LED 켜기
    elif message == "red_off":           # 메시지가 "red_off"이면
        redLed.off()                     # 빨간 LED 끄기

client = mqtt.Client()                   # MQTT 클라이언트 객체 생성
client.on_message = on_message           # 메시지 수신 시 on_message 함수 연결

broker_address = "나의 IP 주소"          # 브로커(라즈베리파이) IP 주소 입력
client.connect(broker_address)           # 브로커에 연결
client.subscribe("led", 1)              # "led" 토픽 구독 등록 (QoS 1)

count = 0                                # 발행할 숫자 초기값 0으로 설정

def send_thread():                       # 1초마다 메시지를 발행하는 스레드 함수
    global count                         # 전역 변수 count 사용 선언
    while 1:                             # 무한 반복
        count = count + 1                # count 1씩 증가
        client.publish("hello", str(count))  # "hello" 토픽으로 count 값 발행
        time.sleep(1.0)                  # 1초 대기 후 반복

task = threading.Thread(target=send_thread)  # send_thread를 별도 스레드로 생성
task.start()                             # 스레드 시작 (발행 + 구독 동시 실행)

client.loop_forever()                    # 메시지 수신 무한 대기 루프 실행
