def get_lines(nombre,ejemplo):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    if(ejemplo):
        nombre = "ejemplo" + nombre
    lines = open('inputs/' + nombre + '.txt',"r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
        lines[i] = lines[i].split(" ")
    return lines

strength_card = {"A":0, "K":1, "Q":2, "J":3, "T":4, "9":5, "8":6, "7":7, "6":8, "5":9, "4":10, "3":11, "2":12}
# 0 -> AAAA .. 6 -> 23456

strength_hand = [[5,0],
                 [4,1],
                 [3,2],
                 [3,1],
                 [2,2],
                 [2,1],
                 [1,1]]

def get_hand(line):
    # Crear un diccionario para almacenar la frecuencia de cada elemento
    frecuencias = {}

    # Recorrer la lista y contar las ocurrencias de cada elemento
    for elemento in line:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1

    list_num = []
    for elem in frecuencias:
        list_num.append([frecuencias[elem],elem])

    list_num = sorted(list_num,reverse=True)

    i=0
    for strength in strength_hand:
        if list_num[0][0] != 5:
            if [list_num[0][0],list_num[1][0]] == strength:
                return [i,line]
        else:
            return [i,line]
        i+=1

def get_ranks(lines):
    total_ranking = []
    dic_hand_points = {}
    for elem in lines:
        if elem[0] not in dic_hand_points:
            dic_hand_points[elem[0]] = elem[1]

    list_ranks = []
    for line in lines:
        list_ranks.append(get_hand(line[0]))
    list_ranks = sorted(list_ranks)

    dic_ranks = {}
    for rank in list_ranks:
        if rank[0] in dic_ranks:
            dic_ranks[rank[0]].append(rank[1])
        else:
            dic_ranks[rank[0]] = [rank[1]]

    for hand_dic in dic_ranks:
        v = dic_ranks[hand_dic]
        long = len(v) - 1
        # haremos long - 1 pasadas : 10 elementos -> 9 pasadas
        for pasada in range (0 , long ) :
            # en cada pasada comparamos el elemento i con el i+1
            for i in range (0 , long - pasada ) :
            # cambiamos de posicion si el izquierdo es menor en fuerza de carta,
            # para ordenar ascendente
                encontrada = False
                j=0
                while not encontrada and j<5:
                    if(strength_card[v[i][j]] > strength_card[v[i+1][j]]):
                        v[i] , v[i +1] = v[i+1] , v[i]
                        encontrada=True
                    elif (strength_card[v[i][j]] != strength_card[v[i+1][j]]):
                        encontrada=True
                    j+=1

    for hands in dic_ranks:
        list_hands = dic_ranks[hands]
        for hand in list_hands:
            total_ranking.append([hand,dic_hand_points[hand]])

    return total_ranking

def get_result(list_numbers):
    sum = 0
    long = len(list_numbers)
    for i in range(long):
        sum += (long - i) * int(list_numbers[i][1])
    return sum

def main(input,ejemplo):
    lines=get_lines(input,ejemplo)
    list_ranks = get_ranks(lines)
    total_points = get_result(list_ranks)
    return total_points

#Probador
print(main("7",False))
