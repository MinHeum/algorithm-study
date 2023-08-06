plates = input()
prev = ""
height = 0
for i in range(len(plates)):
    if prev != plates[i]:
        height+=10
    else:
        height+=5
    prev = plates[i]
print(height)