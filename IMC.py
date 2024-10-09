nome= input("Digite o seu nome completo:")
altura= float(input("Digite a sua altura:"))
peso=int(input("Digite o seu peso:"))

imc= peso/altura**2



nome_cap=nome.title()


    
         



print('Nome:{}'.format(nome_cap))
print('Altura={}'.format(altura))
print('Peso={}' .format(peso))
print('IMC={}'.format(imc))



if imc < 18.5:  
        print ("Abaixo do peso")
elif imc >18.5 and imc < 24.9:  
        print ("Peso normal" ) 
elif imc > 25 and  imc < 29.9:  
        print ("Sobrepeso") 
else:  
        print ("Obesidade")


print("Olá!! {}".format(nome_cap))
print("Lembre-se que o calculo do IMC não calcula percentual de gorduara corporal.")

