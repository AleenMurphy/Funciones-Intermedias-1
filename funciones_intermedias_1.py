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
