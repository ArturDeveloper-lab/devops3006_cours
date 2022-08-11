names = ["chanan", "tom", "zack", "aharon"]
# range(start, end, step)
for i in range(len(names)):
    names[i] = "dotan"

for name in names:
    if name == "zack":
        continue
    print(name)

# a = 0
# while a < 5:
#     print(a)

