
import random

print("Pedro responde, pedro se comunicara con los espiritus que estas cerca de ti, para darte repuesta a tus pregunta")
Pregunta = input("PREGUNTA:  ")

num = random.randint (1, 8)

if num == 1:
    p = "Sí, definitivamente."
elif num ==2:
    p ='Es decididamente así.'
elif num == 3:
    p ="Sin duda."
elif num == 4:
    p = ("Pregunta confusa, inténtalo de nuevo.")
elif num ==5:
    p = ("Pregunta nuevamente más tarde.")
elif num ==6:
    p = ("Mejor no te lo digo ahora.")
elif num ==7:
    p = ("Mis fuentes dicen que no.")
elif num ==8:
    p = ("Las perspectivas no son tan buenas.")
else:
    p = ("Error {num}")

print (f"Pedro responde {p}")


    



