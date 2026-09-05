# Creamos un archivo de texto con los datos entregados en el enunciado

datos = """3.141590000000000094e-03 2.557680595776000416e+02 4.501400409434224770e+01
6.283180000000000189e-03 3.752818426478838205e+02 2.947770471609068110e+01
9.424770000000000716e-03 4.246697882492646841e+02 2.843524433400840579e+01
1.256636000000000038e-02 4.676325636948347437e+02 2.576223788106328882e+01
1.570795000000000177e-02 4.820912691815412359e+02 1.530261598082400276e+01
1.884954000000000143e-02 4.337667969674867550e+02 1.450243036000263963e+01
2.199113000000000109e-02 4.299064323187142804e+02 7.689521175184014012e+00
2.513272000000000075e-02 3.840742743415148084e+02 5.880658615460115257e+00
2.827431000000000041e-02 3.464876766126099596e+02 5.062040746246734280e+00"""

with open("simulacion.txt", "w") as file:
    file.write(datos)

# Importamos el módulo
import h5py

def convertir_a_hd5(nombre_txt, nombre_hd5):

    # Creamos listas vacías para guardar las tres columnas
    datos1 = []
    datos2 = []
    datos3 = []

    # Abrimos el archivo de texto en modo lectura
    with open(nombre_txt, "r") as file:

        # Leemos cada línea del archivo
        for linea in file:

            # Separamos los tres valores de cada fila
            d1, d2, d3 = linea.split()

            # Convertimos los valores a números y los guardamos
            datos1.append(float(d1))
            datos2.append(float(d2))
            datos3.append(float(d3))

    # Creamos el archivo HDF5
    with h5py.File(nombre_hd5, "w") as file:

        # Creamos un dataset para cada columna
        d1 = file.create_dataset("datos1", data=datos1)
        d2 = file.create_dataset("datos2", data=datos2)
        d3 = file.create_dataset("datos3", data=datos3)


# Usamos la función
convertir_a_hd5("simulacion.txt", "simulacion.hd5")

# Comprobamos que los tres datasets se guardaron correctamente
with h5py.File("simulacion.hd5", "r") as file:

    d1 = file["datos1"]
    d2 = file["datos2"]
    d3 = file["datos3"]

    print(d1[:])
    print(d2[:])
    print(d3[:])
