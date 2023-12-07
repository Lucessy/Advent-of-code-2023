def get_lines(nombre):
    '''OBJ = Recoge los datos de un texto y los convierte a una lista'''
    
    lines = open('inputs/' + nombre + '.txt',"r").readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace("\n","")
    return lines

def numeros_ad(line):
    pass

def suma_numeros_ad(lines):
    suma=0
    linea_ant=[]
    linea_act=[]
    numero_str=""
    indice=0
    grid=[]

    for i in range(len(lines)):
        line=lines[i]
        line=list(line)
        for char in line:
            if char != ".":
                if char.isdigit():
                    numero_str+=char
                else:
                    if numero_str != "":
                        #for i in range(len(numero_str)-1):
                        #    linea_act.append(".")
                        linea_act.append(numero_str)
                        numero_str=""
                    linea_act.append(char)
            else:
                if numero_str != "":
                    #for i in range(len(numero_str)-1):
                    #    linea_act.append(".")
                    linea_act.append(numero_str)
                    numero_str=""
                linea_act.append(char)

        if numero_str != "":
            linea_act.append(numero_str)
            numero_str=""
        
        print(linea_act)


        long_act = len(linea_act)

        for i in range(long_act):
            if not linea_act[i].isdigit() and linea_act[i]!=".":
                if i==0:
                    if linea_act[i+1]!=".":
                        suma += int(linea_act[i+1])

                elif i==long_act:
                    if linea_act[i-1]!=".":
                        suma += int(linea_act[i-1])

                else:
                    if linea_act[i-1]!=".":
                        suma += int(linea_act[i-1])
                    if linea_act[i+1]!=".":
                        suma += int(linea_act[i+1])
        
        linea_ant = linea_act
        linea_act = []
        grid.append(linea_ant)

    return suma
            
def main(nombre_input):
    lines = get_lines(nombre_input)
    suma = suma_numeros_ad(lines)
    return suma

#Probador
print(main("ejemplo3"))