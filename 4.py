def get_lines(nombre):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open('inputs/' + nombre + '.txt',"r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines

def get_list_cards(line):
    list_num_have = []
    list_num_won = []
    line=line.split(": ")
    line[1]=line[1].split(" | ")
    line[1][0]=line[1][0].split(" ")
    line[1][1]=line[1][1].split(" ")
    for num in line[1][0]:
        if num!="":
            list_num_won.append(int(num))
    for num in line[1][1]:
        if num!="":
            list_num_have.append(int(num))
    return [list_num_won,list_num_have]

def get_points(card_game):
    suma=0
    for num in card_game[1]:
        if num in card_game[0]:
            if suma==0:
                suma+=1
            else:
                suma*=2
    return suma

def main(input):
    lines=get_lines(input)
    card_game=[]
    suma=0
    for line in lines:
        card_game=get_list_cards(line)
        suma+=get_points(card_game)
    return suma
    

#Probador
print(main("4"))