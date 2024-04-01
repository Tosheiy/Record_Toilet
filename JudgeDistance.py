from machine import Pin
import utime

#DistanceCal関数から少し改良
#distance変数を返す代わりに20cm以上なら１を未満なら０を返す
def judge_distance():
    trigger = Pin(14, Pin.OUT)
    echo = Pin(15, Pin.IN)

    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep(0.00001)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    #計算
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print(str(distance) + "cm")

    #distanceから座っている状態か判別する
    if distance <= 50:
        status = 1
    else:
        status = 0
    return status