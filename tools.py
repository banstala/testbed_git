from datetime import datetime

def time_now(message="\nToday is"):
    print (message, datetime.now().strftime("%d %b %Y"), end=' (')
    print (datetime.now().strftime("%H:%M"), end=')\n\n')
    
    return
