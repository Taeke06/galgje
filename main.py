import random
print("Welkom bij Galgje!\nGalgje is een spel waar je een woord moet raden die de computer hier heeft uitgekozen.")
woordenlijst= ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit" , "heesterperk"]
woord= random.choice (woordenlijst)
print (woord) 

letter = input ("kies een letter\n")
