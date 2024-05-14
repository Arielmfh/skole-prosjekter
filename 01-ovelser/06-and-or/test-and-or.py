import random
a = random.randint(1,2)
b = 1

if a == 1 and b == 1:
    print("Hvis både a og b er lik 1, blir hele testen sann")

if a == 1 or b == 1:
    print("Hvis en av variablene a eller b er lik 1, blir hele testen sann")

innverdi = int(input("Oppgi et tall mellom 1 og 10: "))
test = False

while test == False:
  if innverdi <= 10 and innverdi >= 1:
    test == True
    print ("Tallet du oppga var inennfor.")
    break
  elif innverdi <= 0 or innverdi >= 10:
    print("Tallet må være fra 1 til 10, prøv igjen")
    innverdi = int(input("Oppgi et tall mellom 1 og 10: "))
    