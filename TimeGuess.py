import time
import threading
import Assets
import random

#target_seconds = int(input("please enter the target number of seconds: "))
target_seconds = 0
while target_seconds < 5:
    target_seconds = int(random.random() * 40)
seconds = 0
margin = 2
distraction_oftenness = 7.5
time_in_second = 1
Play = True
input(f"Count in your head to guess when the target amount of time has passed \nYou need to be within {margin} seconds of the target to win \nThe target seconds to count to is: {target_seconds} \n[press enter to start]")


def timer():
    global seconds, Play
    for i in [3,2,1,Assets.GO()]:
        print(i)
        time.sleep(1)
    distractionthread.start()
    userthread.start()
    while Play:
        seconds += 1
        time.sleep(time_in_second)
        if seconds > target_seconds + 10:
            print("Too much time spent, you're 10 seconds over")
            Play = False


def distractions():
    while Play:
        print(random.choice(Assets.Numbers()))
        timetosleep = random.random() * distraction_oftenness
        if timetosleep < 0.3:
            timetosleep += 1
        time.sleep(timetosleep)


def user():
    global seconds, Play
    while Play:
        input() #stall until user presses enter (end game)
        Play = False
        print(f"{seconds} seconds have passed\n")
        seconds_away = abs(target_seconds - seconds)
        print(f"that is {seconds_away} seconds away from the target of {target_seconds} seconds.")
        if seconds_away <= margin :
            print("Well done! You passed!")
        if seconds_away == 0:
            print("Well done! Right on!")
        if seconds > 2 * target_seconds:
            print("That's over double the amount of time! are you alright?")

        shop()


def shop():
    print(Assets.SHOP())



timerthread = threading.Thread(target=timer)
userthread = threading.Thread(target=user)
distractionthread = threading.Thread(target=distractions)
timerthread.start()
