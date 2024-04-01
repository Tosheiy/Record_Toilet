import network
from time import sleep
from dotenv import load_dotenv
import os

# Wi-Fi ルーターのSSIDとパスワード
# 自分の環境に書き換えてください。
def connect():
    load_dotenv()
    ssid = os.getenv('ssid')
    password = os.getenv('password')
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    #ネットワークがアクティブか？
    wlan.active(True)
    #接続
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    #ifconfig()には　IPアドレス、サブネットマスク、デフォルトゲートウェイ　など合計４個が格納
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip