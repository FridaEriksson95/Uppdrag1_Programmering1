import random

#Öppningsmeddelande
print("Välkommen till Gissa Talet!")
print("Du ska nu gissa ett tal mellan 1 och 100, varsågod..")
#Här ska användaren gissa ett tal mellan 1 och 100
guess = int(input("Skriv in ett tal: "))

#Det utvalda numret
SlumpTal = random.randint(1,100)

#om användaren gissar rätt
if guess == SlumpTal:
  print("Grattis, du gissade rätt!")
if guess < SlumpTal:
  
#om användaren gissar för lågt
  print("Tyvärr du gissade för lågt")
if guess > SlumpTal:
  
#om användaren gissar för högt
  print("Tyvärr du gissade för högt")
  
#om användaren är väldigt nära
elif guess == SlumpTal + 3 or guess == SlumpTal - 3:
  print("Du är dock nära och det bränns..")
  
#Nytt försök.
new_guess = int(input("Försök igen: "))

#Nytt försök. Om användaren gissar rätt
if new_guess == SlumpTal:
  print("Grymt jobbat, du gissade rätt!")
  
#Nytt försök. Om användaren gissar för lågt.
elif new_guess < SlumpTal:
  print("Tyvärr du gissade för lågt, bättre lycka nästa gång!")
  
#Nytt försök. Om användaren gissar för högt.
elif new_guess > SlumpTal:
  print("Tyvärr du gissade för högt, bättre lycka nästa gång!")
  
#Nytt försök. Om användaren gissar 10 över eller 10 under rätt svar.
elif new_guess == SlumpTal - 10:
  print("Du är dock nära, men fortfarade felaktigt. Bättre lycka nästa gång!")
elif new_guess == SlumpTal + 10:
  print("Du är dock nära, men lite för högt. Bättre lycka nästa gång!")


input("Tryck Enter för att avsluta programmet..")
