data=[120, 1, 120, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20]
part=98/(len(data)+9)   
amount=data[0]/30+data[1]+data[2]/30+sum(data[3:len(data)-1])+int(data[len(data)-1]/5)
print(amount*part)
# print(test[3:len(test)-1])