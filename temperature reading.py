temperature_reading = [10 -10,70,60,45,80,25]
total = 0
count = 0
for temp in temperature_reading:
 if (temp>80):
    break
 if(temp>50,temp<-10):
    continue
total = total + temp
count = count + 1
if count>0:
    avg = total/count
    print(avg)
else:
    print("count is less than 0")    
