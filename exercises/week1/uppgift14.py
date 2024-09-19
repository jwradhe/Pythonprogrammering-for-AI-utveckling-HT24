from random import randint

slumptal = randint(1,101) 

while True:

    gissning = int(input("Gissa vilket tal jag tänker på: "))

    if gissning == slumptal:
        print(f"Du gissade rätt! Numret var {slumptal}")
        break
    elif gissning < slumptal:
        print("Det var fel, lite högre!")
    elif gissning > slumptal:
        print("Det var fel, lite lägre!")
    
