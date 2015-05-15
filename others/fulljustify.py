__author__ = 'yangpeiwen'

def fulljustify(words, maxWidth):
    if len(words) == 0:
        return []
    if len(words[0]) == 0:
        space = ""
        for i in range(maxWidth):
            space += " "
        return [space]
    rec = []

    nowrec = words[0]
    words2 = words[1:]
    for word in words2:
        if len(nowrec) + len(word) + 1 <= maxWidth:
            nowrec += " " + word
        else:
            rec.append(nowrec)
            nowrec = word
    if len(nowrec) > 0:
        rec.append(nowrec)

    for i in range(len(rec) - 1):
        lastspacewz = 0
        addnum = 1
        if (rec[i].find(" ") == -1) & (len(rec[i]) < maxWidth):
            rec[i] += " "
        while len(rec[i]) < maxWidth:
            nowspacewz = rec[i].find(" ", lastspacewz) + addnum  # 寻找空格
            # print rec[i][:nowspacewz] + "|" + rec[i][nowspacewz:]
            rec[i] = rec[i][:nowspacewz] + " " + rec[i][nowspacewz:]  # 添加空格
            lastspacewz = nowspacewz + 1
            if rec[i].find(" ", lastspacewz) == -1:
                lastspacewz = 0
                addnum += 1
    while len(rec[len(rec) - 1]) < maxWidth:
        rec[len(rec) - 1] += " "
    return rec


print fulljustify([], 0)
print fulljustify([""], 0)
print fulljustify([""], 2)
print fulljustify(["a"], 1)
print fulljustify(["a"], 2)
print fulljustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print fulljustify(["What", "must", "be", "shall", "be."], 12)
print fulljustify(["Here", 'is', "an", "example", "of", "text", "justification."], 14)