def get_lines(nombre):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open('inputs/' + nombre + '.txt',"r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines

def suma_numeros(lines):
    ''' Devuelve el primer numero de una linea'''
    suma = 0
    numbers_list = []
    for line in lines:
        numbers_list = [char for char in line if char.isdigit()]
        if len(numbers_list) != 0:
            num = numbers_list[0] + numbers_list[-1]
        suma += int(num)
        numbers_list = []
    return suma

def main(nombre_input):
    lines = get_lines(nombre_input)
    suma = suma_numeros(lines)
    return suma
        
 
#Probador
print(main("ejemplo1"))