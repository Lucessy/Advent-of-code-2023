def get_lines(nombre):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open('inputs/' + nombre + '.txt',"r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines

def get_seed(line):
    seed_list=[]
    line=line[7:].split(" ")
    for num in line:
        seed_list.append(int(num)) #Convertimos los números en enteros
    return seed_list

def get_range_num(lines,i):
    seed_num=0
    map_num=0
    range_num=0
    salto_pag=False
    list_convertions=[]
    if i==0:
        i=3
    while i<len(lines) and not salto_pag: #Cuando encuentre el espacio en blanco es porque ya acabó la tabla
        if lines[i]!="":
            lines[i]=lines[i].split(" ")

            seed_num=int(lines[i][1])
            map_num=int(lines[i][0])
            range_num=int(lines[i][2])
                            #Rango:   Inicio        Final             Map
            list_convertions.append([seed_num,seed_num+range_num-1,map_num])
            i+=1
        else:
            salto_pag=True
    i+=2
    return list_convertions,i

def get_convertion_num(list_range_num,seeds):
    list_convert_num=[]
    num_found = False
    for seed in seeds:
        for num_range in list_range_num:
            if seed>=num_range[0] and seed<=num_range[1] and not num_found:
                difference=abs(seed-num_range[0])
                list_convert_num.append(num_range[2]+difference)
                num_found = True
        if not num_found:
            list_convert_num.append(seed)
        num_found = False

    return list_convert_num

def get_last_map(lines,seeds):
    tuple_range_i=()
    list_range_num=[]
    list_convert_num=[]
    i=0
    while i<len(lines):
        tuple_range_i=get_range_num(lines,i)
        list_range_num=tuple_range_i[0]
        i=tuple_range_i[1]
        list_convert_num=get_convertion_num(list_range_num,seeds)
        seeds=list_convert_num
    return seeds

def main(input):
    #Obtenemos la lista de lineas
    lines=get_lines(input) 
    #Obtenemos las seed de la primera línea
    seeds=get_seed(lines[0])
    #Obtenemos el valor mínimo de la última conversión
    location_map=get_last_map(lines,seeds)

    return min(location_map)


#probador
print(main("5"))