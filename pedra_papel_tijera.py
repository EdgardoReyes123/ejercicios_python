import random
options = ('piedra', 'papel','tijera')
computer_option = random.choice(options)
user_option = input("piedra, papel o tijera: ").lower()

while True:
    if user_option == computer_option:
        print ("Empate!")
        break

    if user_option =="piedra" and computer_option=="papel":
        print ("Gano computer...")
        print("Papel le gana a piedra")
        break

    if user_option =="piedra" and computer_option=="tijera":
        print ("Gano usuario...")
        print("Piedra le gana a tijera")
        break
        
    if user_option =="papel" and computer_option=="piedra":
        print ("Gano el Usuario...")
        print("Papel le gana a piedra")
        break


        
  
    if user_option =="papel" and computer_option=="tijera":
        print ("Gano el computer...")
        print("Pijera le gana a papel") 
        break 


    
    if user_option =="tijera" and computer_option=="papel":
        print ("Gano Usuario...")
        print("Tijera le gana a papel")
        break
    
    if user_option =="tijera" and computer_option=="piedra":
        print ("Gano computer...")
        print("Piedra le gana a tijera")
        break

    
    
