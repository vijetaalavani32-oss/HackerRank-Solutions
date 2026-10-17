import re
def fun(s):
     pattern = r'^[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'
     return re.match(pattern, s) is not None

    # return True if s is a valid email, else return False

