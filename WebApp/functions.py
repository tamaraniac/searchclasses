def timeConvert(string):
    if string == None or string == '':
        return None
    # Assume input is good
    h = int(string[0: 2])
    m = int(string[3: 5])
    if string[6] == 'P':
        if h != 12:
            h += 12
    elif string[6] == 'A':
        if h == 12:
            h = 0

    time = h * 100 + m
    return time

def inString(small, big):
    for char in small:
        if char not in big:
            return False
    return True
