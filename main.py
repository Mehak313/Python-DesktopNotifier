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

      
        
