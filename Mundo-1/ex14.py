# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Insira a temperatura em °C: '))
f = (c * 9/5) + 32 
print(f'{c}°C corresponde a {f:.2f}°F')