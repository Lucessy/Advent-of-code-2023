import numpy as np
import time
inicio = time.time()

def get_lines(nombre):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open('inputs/' + nombre + '.txt',"r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines

def get_seed(line):
    seed_list=[]
    line=line[7:].split(" ")
    for i in range(0,len(line),2):
        seed_list.append([int(line[i]),int(line[i+1])]) #Convertimos los numeros en pares de rangos
    return seed_list

def get_range_num(lines):
    seed_num=0
    map_num=0
    range_num=0
    list_convertions=[]
    num_range=[]
    i=3
    while i<len(lines): #Cuando encuentre el espacio en blanco es porque ya acabó la tabla
        if lines[i]!="":
            lines[i]=lines[i].split(" ")

            seed_num=int(lines[i][1])
            map_num=int(lines[i][0])
            range_num=int(lines[i][2])
                            #Rango:   Inicio        Final             Map
            num_range.append([seed_num,seed_num+range_num-1,map_num])
            i+=1
        else:
            list_convertions.append(num_range)
            num_range=[]
            i+=2
    list_convertions.append(num_range)
    return list_convertions

def get_convertion_num(list_range_num,seeds):
    list_convert_num=[]
    num_found = False

    for seed in seeds:
        i = 0
        while not num_found and i < len(list_range_num):
            num_range = list_range_num[i]
            if seed>=num_range[0] and seed<=num_range[1]:
                difference=abs(seed-num_range[0])
                list_convert_num.append(num_range[2]+difference)
                num_found = True
            i += 1
        if not num_found:
            list_convert_num.append(seed)
        num_found = False

    return list_convert_num


def get_last_map(list_convertions,seeds):
    list_convert_num=[]
    for range in list_convertions:
        list_convert_num=get_convertion_num(range,seeds)
        seeds=list_convert_num
    return seeds

def get_min_num_per_load(seeds,list_convertions,limite):
    contador=0
    k=0
    list_seeds=[]
    minimos=[]
    mini=0
    #Calculamos los valores por lotes con un contador y un limite
    while k<len(seeds):
        for seed in seeds:
            #[79 , 14]      79      93-1
            #[55 , 13]      55      68-1
            inicio=seed[0]
            fin=seed[0]+seed[1]
            print(inicio,fin)
            for j in range(inicio,fin):
                if contador%limite==0 or j==fin-1:
                    list_seeds.append(j)
                    location_map=get_last_map(list_convertions,list_seeds)
                    minimos.append(min(location_map))
                    list_seeds=[]
                else:
                    list_seeds.append(j)
                contador+=1
            mini=min(minimos)
            minimos=[]
            minimos.append(mini)
            print(f"TANDA COMPLETA: {contador}")
        k+=1
    return minimos

def main(input,limite):
    #Obtenemos la lista de lineas
    lines=get_lines(input) 
    #Obtenemos las seed de la primera línea
    seeds=get_seed(lines[0])
    #Obtenemos la lista con los rangos de numero a convertir
    list_convertions=get_range_num(lines)
    #Llamada a calcular por rangos el mínimo
    minimos=get_min_num_per_load(seeds,list_convertions,limite)
    #Obtenemos el valor mínimo de los minimos de cada lote de conversión
    return min(minimos)


#probador
print(main("5",100))
fin = time.time()
print(f"El tiempo total de ejecución del programa es {fin - inicio} seg")