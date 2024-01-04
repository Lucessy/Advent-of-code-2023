def get_lines(nombre,ejemplo):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    if(ejemplo):
        nombre = "ejemplo" + nombre
    lines = open('inputs/' + nombre + '.txt',"r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
        lines[i] = lines[i].split(" ")
    return lines

strength_card = {"A":0, "K":1, "Q":2, "T":4, "9":5, "8":6, "7":7, "6":8, "5":9, "4":10, "3":11, "2":12, "J":13}
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

    # Verificamos si hay Jokers y añadimos el número de jokers a la mayor combinación que no sea Jokers
    joker = False
    i = 0
    for hand in list_num:
        if hand[1] == "J" and hand[0] != 5:
            while not joker:
                if list_num[i][1] != "J":
                    list_num[i][0] += hand[0]
                    joker = True
                i+=1  
            list_num.remove([hand[0],hand[1]])

    j = 0 
    for strength in strength_hand:
        if list_num[0][0] != 5:
            if [list_num[0][0],list_num[1][0]] == strength:
                return [j,line]
        else:
            return [j,line]
        j+=1

def get_ranks(lines):
    total_ranking = []
    dic_hand_points = {}
    # Guardamos la combinación y su puntuación en un diccionario
    for elem in lines:
        if elem[0] not in dic_hand_points:
            dic_hand_points[elem[0]] = elem[1]

    # Obtenemos el rango de la combinación de 0 a 6 y luego lo ordenamos por rango de menor a mayor
    list_ranks = []
    for line in lines:
        list_ranks.append(get_hand(line[0]))
    list_ranks = sorted(list_ranks)

    # Agrupamos por rango en un diccionario
    dic_ranks = {}
    for rank in list_ranks:
        if rank[0] in dic_ranks:
            dic_ranks[rank[0]].append(rank[1])
        else:
            dic_ranks[rank[0]] = [rank[1]]

    # Ordenamos por fuerza de combinación en cada agrupamiento de rango
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

    # Agrupamos cada combinación en orden con su puntuación para la lista final
    for hands in dic_ranks:
        list_hands = dic_ranks[hands]
        for hand in list_hands:
            total_ranking.append([hand,dic_hand_points[hand]])

    return total_ranking

def main(input,ejemplo):
    lines=get_lines(input,ejemplo)
    list_ranks = get_ranks(lines)
    sum = 0
    long = len(list_ranks)
    for i in range(long):
        sum += (long - i) * int(list_ranks[i][1])
    return sum

#Probador
print(main("7",False))
