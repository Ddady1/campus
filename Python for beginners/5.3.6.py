def filter_teens(a=13, b=13, c=13):
    sun = 0
    if a >= 13 and a <= 19 and a != 15 and a != 16:
        num = fix_age(a)
        sun += num
    else:
        sun += a
    if b >= 13 and b <= 19 and b != 15 and b != 16:
        num = fix_age(b)
        sun += num
    else:
        sun += b
    if c >= 13 and c <= 19 and c != 15 and c != 16:
        num = fix_age(c)
        sun += num
    else:
        sun += c
    return sun


def fix_age(age):
    age = 0
    return age