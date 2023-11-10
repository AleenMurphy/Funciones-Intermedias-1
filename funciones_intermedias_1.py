x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Cambia el valor 10 en x a 15
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15

# Cambia el "apellido" del primer alumno de 'Jordan' a 'Bryant'
estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Bryant'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

# Cambia "Messi" por "Andrés"
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Andrés', 'Ronaldo', 'Rooney']
}

# Cambia el valor 20 en z a 30
z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30

print(x)
print(estudiantes)
print(directorio_deportes)
print(z)

#Iterar a través de una lista de diccionarios

def iterateDictionary(some_list):
    for dictionary in some_list:
        output = ""
        for key, value in dictionary.items():
            output += f"{key} - {value}, "
        print(output[:-2])

# Ejemplo de uso con la lista de estudiantes
estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(estudiantes)

# Obtener valores de una lista de diccionarios
def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])

# Ejemplo de uso con la lista de estudiantes y la clave 'first_name'
estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

# Iterar a través de un diccionarios con valores de lista
def printInfo(some_dict):
    for key, values in some_dict.items():
        print(len(values), key.upper())
        for value in values:
            print(value)
        print()

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
