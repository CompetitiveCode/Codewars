# Answer to Human Readable Time
# https://www.codewars.com/kata/human-readable-time/python


def make_readable(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    return f'{h:02d}:{m:02d}:{s:02d}'

