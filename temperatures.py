temperatures = [155,168,180,192,198,205]
for temp in temperatures:
    if temp < 150 or temp > 200:
        print("error:unsafe temperature = ",temp)
        break
    else:
        print("branch approved")