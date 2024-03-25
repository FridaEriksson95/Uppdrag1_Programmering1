#Öppningsfras
print("Välkomna till denna pensionssimulator!")

x = 65

#Be användaren skriva sitt namn
print("Skriv in ditt namn: ")
name = input()

#Be användaren skriva in sin ålder
print ("Hej " + name)
print("Hur gammal är du? ")
age = input()

#Räkna ut hur många år det är kvar till pension
if int(age) < 65:
  print(name + ", du går i pension om " + str(65 - int(age)) + " år.")

#Om användaren är 65 år eller äldre
elif int(age) > 65:
  print(name + ", du har redan uppnått pensionsålder.")
  
input("Tack för ditt deltagande. Tryck enter för att avsluta programmet..")