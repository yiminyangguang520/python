__author__ = 'yangpeiwen'

def zhongjian(yourstr, leftstr, rightstr):
    leftposition = yourstr.find(leftstr)
    rightposition = yourstr.find(rightstr, leftposition+len(leftstr))
    return yourstr[leftposition+len(leftstr):rightposition]
    # 取文本中间内容