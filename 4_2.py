import time
inicio = time.time()
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

def get_copies(card_game):
    suma=0
    for num in card_game[1]:
        if num in card_game[0]:
                suma+=1
    return suma

def get_total_copies(list_copies_games,i):
    if list_copies_games[i]==0: return 0
    else:
        num_copie=list_copies_games[i]
        for j in range(1,num_copie+1):
            num_copie+=get_total_copies(list_copies_games,i+j)
        return num_copie
        
def main(input):
    lines=get_lines(input)
    card_game=[]
    list_copies_games=[]
    total_num_copies=0

    for line in lines:
        card_game=get_list_cards(line)
        list_copies_games.append(get_copies(card_game))

    for i in range(len(list_copies_games)):
        total_num_copies+=get_total_copies(list_copies_games,i)
    
    return total_num_copies+len(list_copies_games)

#Probador
print(main("4"))
fin = time.time()
print(f"El tiempo total de ejecución del programa es {fin - inicio} seg")