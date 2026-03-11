nombre_usuario = input('ingrese su nombre')
puntaje = 0

print(f'bienvenido {nombre_usuario}')

pregunta1 = input('cual es el nombre del coach de cabello largo?')
if pregunta1 == 'olaf':
    puntaje = puntaje + 1
pregunta2 = input('cual es el color de su cabello?')
if pregunta2 == 'negro':
    puntaje = puntaje + 1
pregunta3 = input('que tipo de cabello tiene?. Lacio, rizado o afro?')
if pregunta3 == 'rizado':
    puntaje = puntaje + 1
pregunta4 = input('que shampoo usa?. Pantene, Head&Shoulders o Sedal')
if pregunta4 == 'Sedal':
    puntaje = puntaje + 1

if puntaje == 4:
    print('Excelente')
elif puntaje >= 2 :
    print('Muy bien')
else:
    print('Puedes mejorar')