import time
from plyer import notification 



if __name__=="__main__":
    while True:
        notification.notify(
            title="Please Drink Water.",
            message="Drinking water is very important for your health.",
            timeout=5
        )
        notification.notify(
            title="Take a break!",
            message="Working too long without taking a break can take a toll on your health. Therefore, at least 5 minutes in every hour should be spent away from the screen.",
            timeout=7
            )
        time.sleep(60*60)

        print("What shall I remind you about?")
text = str(input())
print("In how many minutes?")
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)
print(text)
        
