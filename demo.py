# coding:UTF-8
biaotou = ['Name', 'Password', 'visit', 'edit', 'delete', 'superuser', 'salt']
shuju = [(u'管理员admin', u'fd2700999139d3ee47ec8b06c0991419', 1, 1, 1, 1, u'ilqzohanzxctroop'),
         (u'guest', u'9c803a59721dc376d27ff5d46bfc5a96', 1, 0, 0, 0, u'rtblqnyzjdytqqzd')]

a = "中文"
print a, type(a)
a = a.decode('utf-8')
print a, type(a)


def encode(head,data):
    enhead = ''
    for evehead in head:
        enhead += str(evehead) + ','

    endata = ''
    for everyone in data:
        for evedata in everyone:
            if type(evedata) == str:
                evedata = evedata.decode('utf-8')
            elif type(evedata) != unicode:
                evedata = str(evedata)
            endata += evedata + ','
        endata += '\n'
    return enhead, endata

head, data = encode(biaotou, shuju)

print head
print data
