nombre_usuario = input('ingrese su nombre: ')
puntaje = 0

print(f'bienvenido {nombre_usuario}')

pregunta1 = input('cual es el nombre del coach de cabello largo?: ')
if pregunta1.lower() == 'olaf':
    puntaje = puntaje + 1
pregunta2 = input('cual es el color de su cabello?: ')
if pregunta2.lower() == 'negro':
    puntaje = puntaje + 1
pregunta3 = input('que tipo de cabello tiene?. lacio, rizado o afro?: ')
if pregunta3.lower() == 'rizado':
    puntaje = puntaje + 1
pregunta4 = input('que shampoo usa?. pantene, head&shoulders o sedal: ')
if pregunta4.lower() == 'sedal':
    puntaje = puntaje + 1

if puntaje == 4:
    print('Excelente!')
elif puntaje >= 2 :
    print('Muy bien!')
else:
    print('Puedes mejorar')