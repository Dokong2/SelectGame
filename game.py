import time
import os
go = True

def home():
    while True:
        print("━━━━━선택 게임━━━━━")
        print("설치 버전 : codeMadeVer 1.0")
        print("게임을 시작하시려면 [start]를 입력하세요.")
        start = input(">>")
        if start == "start":
            print("게임을 시작합니다.")
            break
        else:
            print("? 뭘 입력한거시죠?")

def lode():
    print("게임을 시작합니다.")
    print("5초후 게임이 시작됩니다.")
    time.sleep(1)
    print("4초후 게임이 시작됩니다.")
    time.sleep(1)
    print("3초후 게임이 시작됩니다.")
    time.sleep(1)
    print("2초후 게임이 시작됩니다.")
    time.sleep(1)
    print("1초후 게임이 시작됩니다.")
    time.sleep(1)

def Q1():
    print("당신은 유명한 어쩌구리히타쿠토프레스의겁나쎈짱짱검 을 찾으러 여행을 떠났습니다.")
    time.sleep(1.2)
    print("이제부터 당신에게는 수만은 선택이 있을것입니다.")
    time.sleep(1.2)
    print("거기에서 올바른 선택을 해야만 합니다.")
    time.sleep(1.2)
    print("그럼..출발합니다.")
    time.sleep(4)
    os.system('cls')
    print("DAY 1 ━━━━━ 섬으로 갈 준비하기")
    print("당신은 섬으로 갈 준비를 집에서 할 것입니다.")
    print("섬으로 가기 전 할 준비를 하세요.")
    print("씻는다 [1] ㅣ 씻지 않는다 [2]")
    Q1 = input(">>")
    if Q1 == "1":
        print("당신은 개운하게 씻었습니다.")
        go = True
    elif Q1 == "2":
        print("당신은 씻지 않아서 시공간을 초월한 2030년의 엄마에게 등짝스매싱을 받고 사망했습니다.")
        print("DIE NUMBER : 1")
    else:
        print("당신은 오타를 내어서 더이상 버그를 참지 못하는 개발자에게 죽었습니다.")
        print("DIE NUMBER : -1")
        go = False
    if go == False:
        sys.exit()
    os.system('cls')
    print("당신은 섬에 가져갈 것을 고릅니다.")
    print("무엇을 고를 것입니까?")
    print("식량 [1] ㅣ 곰인형 [2]")
    Q2 = input(">>")
    if Q2 == "1":
        print("배고픔을 해결할 수 있습니다!")
    elif Q2 == "2":
        print("당신은 배고픔보다 따뜻한 곰인형을 더 챙겨가고 싶었습니다. 당신은 굶어 죽었습니다.")
        print("DIE NUMBER : 2")
    else:
        print("당신은 오타를 내어서 더이상 버그를 참지 못하는 개발자에게 죽었습니다.")
        print("DIE NUMBER : -1")

# 항상 아빠만 부르면 버그가 고쳐지드라