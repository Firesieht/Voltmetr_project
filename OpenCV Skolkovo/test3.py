f = open("settins.txt", "r")

sr = list(list(f.readlines()[3].split("\n"))[0].split("QQQ"))

for i in range(len(sr)):
    sr[i] = list(sr[i].split(","))
    for j in range(len(sr[i])):
        sr[i][j] = list(sr[i][j].split(" "))
print(sr)