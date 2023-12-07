def get_lines(nombre):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open('inputs/' + nombre + '.txt',"r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines

def list_num(line):
    list_num=[]
    line=line.split(": ")
    line[1]=line[1].split(" ")
    for sim in line[1]:
        if sim!="":
            list_num.append(int(sim))
    return list_num

def num_ways_to_win(time_list,distance_list):
    time=0
    distance=0
    time_rest=0
    num_wins=0
    list_num_wins=[]
    for i in range(len(time_list)):
        time=time_list[i]
        for v in range(time+1):
            time_rest=time-v
            distance=time_rest*v
            if distance>distance_list[i]:
                num_wins+=1
        list_num_wins.append(num_wins)
        num_wins=0
    return list_num_wins

def main(input):
    lines=get_lines(input)
    time_list=list_num(lines[0])
    distance_list=list_num(lines[1])

    num_wins=num_ways_to_win(time_list,distance_list)

    num_total=1
    for num in num_wins:
        num_total*=num
    return num_total

#Probador
print(main("6"))