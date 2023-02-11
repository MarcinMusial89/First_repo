# def multiply(x, y):
#     if isinstance(x, (int, float)) and isinstance(y,  (int, float)):
#         return round(x * y, 5)
#     else:
#         return round(x * y)
#
#
# def no_of_letter(text):
#     return len(text)

def fissbuzz(input):
    try:
        input = int(float(input))
    except:
        input = 0

    if input <= 0:
        return None
    elif input % 3 == 0:
        return ('fiss')
    elif input % 5 == 0:
        return ('buzz')
    elif input % 3 == 0 and input % 5 == 0:
        return ('fissBuss')
    else:
        return input
