def get_lines(nombre):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open('inputs/' + nombre + '.txt',"r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines

color_cubes = ["red","green","blue"]
num_cubes = [12,13,14]

def es_posible(line):
    line=line.split("; ")
    line[0]=line[0].split(": ")
    line.append(line[0][0][5:])
    line[0]=line[0][1]

    suma_r = 0
    suma_g = 0
    suma_b = 0

    for i in range(len(line)-1):
        sets=line[i]
        set_line = sets.split(", ")
        for set in set_line:
            set=set.split(" ")
            if color_cubes[0] in set:
                if suma_r<int(set[0]):
                    suma_r = int(set[0])

            elif color_cubes[1] in set:
                if suma_g<int(set[0]):
                    suma_g = int(set[0])

            else:
                if suma_b<int(set[0]):
                    suma_b = int(set[0])
    return suma_r*suma_g*suma_b

def suma_ids(lines):
    suma = 0
    for line in lines:
        suma += es_posible(line)
    return suma

def main(input):
    lines = get_lines(input)
    suma = suma_ids(lines)
    return suma

#Probador
print(main("ejemplo2"))