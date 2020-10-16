c = [[['216', '378', '378', '216'], ['83', '83', '175', '175']],
     [['412', '619', '619', '412'], ['112', '112', '190', '190']]]


l = []
f = open('settins.txt', 'a')
for i in c:
    i[0] = " ".join(i[0])
    i[1] = " ".join(i[1])
for i in c:
    i = ",".join(i)
    l.append(i)
l = "QQQ".join(l)
f.write(l + "\n")