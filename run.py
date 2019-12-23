import time
from pyminder.pyminder import Pyminder

def token():
    return open("token.secret").read()

pyminder = Pyminder(user='[your username]', token=token())

goals = pyminder.get_goals()
for goal in goals:
    # Goal objects expose all API data as dynamic properties.
    # http://api.beeminder.com/#attributes-2
    print(goal.slug)
    print(goal.title)
    print(goal.rate)
    print(goal.fineprint)
    print(goal.losedate)


    # Goal objects also implement a handful of helper functions.
    # Note: These functions probably contain bugs! Issues & pull requests welcome.
    # https://github.com/narthur/pyminder/blob/master/pyminder/goal.py
    now = time.time()
    sum_ = goal.get_data_sum(now)
    needed = goal.get_needed(now)

