import machine
import utime
import notion_push
import JudgeDistance
import ConnectWifi

try:
    ConnectWifi.connect()
    cnt = 0
    pause_push = 0
    count_push = 0
    while True:
        print(str(cnt) + "回")
        #20cm以下なら１、上なら０を返す
        judge = JudgeDistance.judge_distance()
        if judge==1:
            cnt += 1
        elif cnt>0 and judge==0:
            cnt -= 1 
        if cnt>=20 and pause_push==0:
            notion_push.notion_push()
            count_push += 1
            pause_push = 1
        if cnt==0:
            pause_push = 0
        utime.sleep(5)
        
except KeyboardInterrupt:
    machine.reset()