def get_lines(nombre):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open('inputs/' + nombre + '.txt',"r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines

lista_numeros = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def suma_numeros(line):
    ''' '''
    numbers_list = []
    prim_num = False
    ult_num=False
    i=0
    j=0
    numero_str = ""

    while not prim_num or not ult_num:
        if not prim_num:
            while i<len(line) and not prim_num:
                if not line[i].isdigit():
                    numero_str += line[i]
                    indice = next((i for i, cadena in enumerate(lista_numeros) if numero_str == cadena), None)
                    if indice is not None:
                        numbers_list.append(indice+1)
                        prim_num=True
                        numero_str=""
                else:
                    if numero_str=="":
                        numbers_list.append(int(line[i]))
                        prim_num = True
                    break
                i+=1
            if not prim_num:
                line=line[1:]
            if len(line)==0:
                prim_num=True
        else:
            while i<len(line) and not ult_num:
                line_inv=line[::-1]
                if not line_inv[j].isdigit():
                    numero_str+=line_inv[j]
                    numero_str_inv=numero_str[::-1]
                    indice = next((i for i, cadena in enumerate(lista_numeros) if numero_str_inv == cadena), None)
                    if indice is not None:
                        numbers_list.append(indice+1)
                        ult_num=True
                        numero_str=""
                else:
                    if numero_str=="":
                        numbers_list.append(int(line_inv[j]))
                        ult_num = True
                    break
                j+=1
            if not ult_num:
                line=line[:-1]
            if len(line)==0:
                ult_num=True

        numero_str=""
        i=0
        j=0

    return int(str(numbers_list[0])+str(numbers_list[-1]))

def suma_total(lines):
    suma = 0
    for line in lines:
        suma += suma_numeros(line)
    return suma

def main(nombre_input):
    lines = get_lines(nombre_input)
    suma = suma_total(lines)
    return suma
        
 
#Probador
print(main("1"))