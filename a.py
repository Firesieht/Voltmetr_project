from array import array
sp = [[array("b",[123,123]),array("b",[123,123]),array("b",[123,123]), array("b",[123, 123])], [array("b",[123,123]),array("b",[123,123]),array("b",[123,123]),array("b",[123,123])]]
for i in range(len(sp)):
    for j in range(len(sp[i])):
        sp[i][j] = list(sp[i][j])
        for x in range(len(sp[i][j])):
            sp[i][j][x] = str(sp[i][j][x])
        sp[i][j] = " ".join(sp[i][j])
    sp[i] = "XXX".join(sp[i])
sp = "QQQ".join(sp)

sp = sp.split("QQQ")
for i in range(len(sp)):
    sp[i] = sp[i].split("XXX")
    for j in range(len(sp[i])):
        sp[i][j] = sp[i][j].split(" ")

print(sp)