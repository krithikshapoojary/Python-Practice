temperature = [155,168,180,192,198,205]
for temp in temperature:
    print("checking temperature",temp)
    if temp < 150 or temp > 200:
        print("error")
        break
else:
    print("batch approved")    