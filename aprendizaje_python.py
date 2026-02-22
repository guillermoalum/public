"""
Guía práctica de Python (nivel inicial)
======================================
Este archivo está pensado para aprender leyendo y ejecutando.
Incluye ejemplos de los conceptos más importantes con comentarios.

Cómo usarlo:
1) Lee cada sección.
2) Ejecuta el archivo: `python3 aprendizaje_python.py`
3) Modifica valores y vuelve a correrlo para ver cambios.
"""

# ------------------------------------------------------------
# 1) VARIABLES Y TIPOS BÁSICOS
# ------------------------------------------------------------
# En Python no hace falta declarar el tipo de una variable.
# El tipo se infiere automáticamente según el valor.

nombre = "Ana"          # str (texto)
edad = 28               # int (entero)
altura = 1.68           # float (decimal)
es_estudiante = True    # bool (booleano)

print("\n--- 1) Variables y tipos ---")
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("¿Es estudiante?:", es_estudiante)


# ------------------------------------------------------------
# 2) OPERADORES
# ------------------------------------------------------------
# Operadores aritméticos: +, -, *, /, //, %, **

numero_a = 10
numero_b = 3

print("\n--- 2) Operadores ---")
print("Suma:", numero_a + numero_b)
print("Resta:", numero_a - numero_b)
print("Multiplicación:", numero_a * numero_b)
print("División:", numero_a / numero_b)        # Resultado float
print("División entera:", numero_a // numero_b)
print("Módulo (resto):", numero_a % numero_b)
print("Potencia:", numero_a ** numero_b)


# ------------------------------------------------------------
# 3) ESTRUCTURAS DE DATOS
# ------------------------------------------------------------

# 3.1 Lista: colección ordenada y mutable
frutas = ["manzana", "banana", "naranja"]
frutas.append("pera")  # Agregamos un elemento al final

# 3.2 Tupla: colección ordenada e inmutable
coordenadas = (10.5, -3.2)

# 3.3 Set: colección NO ordenada y sin duplicados
colores = {"rojo", "verde", "azul", "rojo"}  # "rojo" repetido se guarda una sola vez

# 3.4 Diccionario: pares clave -> valor
persona = {
    "nombre": "Carlos",
    "edad": 35,
    "ciudad": "Madrid",
}
persona["profesion"] = "Ingeniero"  # Agregar nueva clave

print("\n--- 3) Estructuras de datos ---")
print("Lista de frutas:", frutas)
print("Tupla de coordenadas:", coordenadas)
print("Set de colores:", colores)
print("Diccionario persona:", persona)


# ------------------------------------------------------------
# 4) CONDICIONALES (if / elif / else)
# ------------------------------------------------------------

print("\n--- 4) Condicionales ---")
if edad < 18:
    print("Eres menor de edad")
elif edad < 65:
    print("Eres adulto")
else:
    print("Eres adulto mayor")


# ------------------------------------------------------------
# 5) BUCLES (for / while)
# ------------------------------------------------------------

print("\n--- 5) Bucles ---")
print("Recorrer lista con for:")
for fruta in frutas:
    print("-", fruta)

print("Contador con while:")
contador = 1
while contador <= 3:
    print("Iteración", contador)
    contador += 1


# ------------------------------------------------------------
# 6) FUNCIONES
# ------------------------------------------------------------
# Las funciones permiten reutilizar lógica.

def saludar(nombre_usuario):
    """Devuelve un saludo para el nombre recibido."""
    return f"Hola, {nombre_usuario}!"


def dividir_seguro(x, y=1):
    """Divide x entre y. y tiene valor por defecto 1."""
    if y == 0:
        return "No se puede dividir entre cero"
    return x / y


print("\n--- 6) Funciones ---")
print(saludar("Lucía"))
print("10 / 2 =", dividir_seguro(10, 2))
print("10 / 0 =", dividir_seguro(10, 0))


# ------------------------------------------------------------
# 7) COMPREHENSIONS (forma compacta de crear colecciones)
# ------------------------------------------------------------

numeros = [1, 2, 3, 4, 5]
cuadrados = [n ** 2 for n in numeros]
pares = [n for n in numeros if n % 2 == 0]

print("\n--- 7) Comprehensions ---")
print("Números:", numeros)
print("Cuadrados:", cuadrados)
print("Pares:", pares)


# ------------------------------------------------------------
# 8) MANEJO DE ERRORES (try / except)
# ------------------------------------------------------------

print("\n--- 8) Manejo de errores ---")
texto_numero = "abc"

try:
    valor = int(texto_numero)  # Esto generará ValueError
    print("Conversión exitosa:", valor)
except ValueError:
    print(f"No se pudo convertir '{texto_numero}' a entero")


# ------------------------------------------------------------
# 9) CLASES Y OBJETOS (Programación Orientada a Objetos)
# ------------------------------------------------------------

class CuentaBancaria:
    """Ejemplo sencillo de clase con atributos y métodos."""

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return f"Depósito exitoso. Nuevo saldo: {self.saldo}"
        return "El monto debe ser positivo"

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            return f"Retiro exitoso. Nuevo saldo: {self.saldo}"
        return "Fondos insuficientes o monto inválido"


print("\n--- 9) Clases y objetos ---")
cuenta = CuentaBancaria("María", 100)
print("Titular:", cuenta.titular)
print(cuenta.depositar(50))
print(cuenta.retirar(30))
print(cuenta.retirar(500))


# ------------------------------------------------------------
# 10) MÓDULO PRINCIPAL
# ------------------------------------------------------------
# Esta condición permite que cierto código solo se ejecute
# cuando corres este archivo directamente.

if __name__ == "__main__":
    print("\n--- 10) __main__ ---")
    print("Ejecutaste aprendizaje_python.py directamente.")
    print("Tip: cambia variables/ejemplos y vuelve a ejecutar para practicar.")
