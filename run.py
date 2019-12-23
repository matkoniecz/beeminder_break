import time
import datetime
from pyminder.pyminder import Pyminder

def token():
    return open("token.secret").read()

pyminder = Pyminder(user='[your username - dummy field]', token=token())

goals = pyminder.get_goals()

break_start = datetime.datetime(2019,12,23)
break_end = datetime.datetime(2019,12,28)
print("Hello,")
print("")
print("Sadly, it is too late for me to enable a break manually.")
print("I need to request a manual break override - from ", break_start.date(), "to", break_end.date(), "for following goals:")
print("")
for goal in goals:
    # Goal objects expose all API data as dynamic properties.
    # http://api.beeminder.com/#attributes-2

    ep = datetime.datetime(1970,1,1,0,0,0)
    x = (break_end - ep).total_seconds()
    needed = goal.get_needed(x)
    if needed > 0:
        print(goal.slug)
        #print(goal.title)
        #print(goal.fineprint)
        #print(goal.losedate) # unix timestamp


    # Goal objects also implement a handful of helper functions.
    # Note: These functions probably contain bugs! Issues & pull requests welcome.
    # https://github.com/narthur/pyminder/blob/master/pyminder/goal.py
    now = time.time()
    sum_ = goal.get_data_sum(now)
    needed = goal.get_needed(now)

