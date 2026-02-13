import pyautogui as pg

import time as t



# FALSE 

pg.FAILSAFE = False



# 좌표 리스트를 생성합니다.

coordinates = [

    (410, 75),   # 한국본사 좌표

    (520, 75),   # SUSEHQUF VNAWLFGUSGHKD

    (750, 75),   # 일자별 좌표

    (850, 75),   # 기간별 좌표

    (1280, 75),  # infor 코드

    (1380, 75),  # 게시판 코드

    (1450, 75),  # 동영상 코드

    (1450, 200)  # 클릭 코드

]



# 반복 실행할 시간 간격을 설정합니다.

interval = 30  # 59초마다 순환



# 초기 대기 시간을 설정합니다.

initial_delay = 58



# 초기 대기 시간을 기다립니다.

t.sleep(initial_delay)



# 무한 루프로 클릭 순환을 실행합니다.

while True:

    # 좌표 리스트를 순환하면서 클릭합니다.

    for coord in coordinates:

        pg.click(coord[0], coord[1], duration=5)



        # 현재 좌표가 클릭 코드인 경우

        if coord == (1450, 200):

            # 59초 동안 기다립니다.

            t.sleep(59)



        # 나머지 좌표의 경우는 30초 간격으로 순환합니다.

        else:

            t.sleep(interval)


