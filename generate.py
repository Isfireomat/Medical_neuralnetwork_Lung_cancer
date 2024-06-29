import numpy as np
from random import randint

def generate_data(num_samples):
    countries = [
        "Angola", "Brazil", "Kenya", "Congo", "Lesotho", "Cambodia", "Ethiopia", 
        "DR Congo", "Liberia", "Namibia", "Myanmar", "Philippines", "Sierra Leone", 
        "Zambia", "Zimbabwe", "Tanzania", "Thailand", "Mozambique", "Pakistan", 
        "Papua New Guinea", "Central African Republic"
    ]
    # 
    datas=[]
    for _ in range(num_samples):
        age=randint(1,120)
        smoking=randint(0,age)
        data=[age,randint(0,1),smoking]
        for _ in range(14):
            data.append(randint(0,1))
        data.append(randint(0,len(countries)))
        
        part=98/(len(data)+9)   
        amount=data[0]/30+data[1]+data[2]/30+sum(data[3:len(data)-1])+int(data[len(data)-1]/5)
        data.append(round(amount*part,2))    
            
        
        
        datas.append(data)
    return datas
        
    
def save_to_file(data, filename):
    with open(filename, 'w') as file:
        for sample in data:
            file.write(str(sample) + '\n')

num_samples = 500_000
data = generate_data(num_samples)

# Save to text file
filename = 'Датасет5.txt'
save_to_file(data, filename)
