def calcular_divisao(dividendo, divisor):
    # Calcula o resultado da divisão
    resultado_normal = dividendo / divisor
    resultado_inteiro = dividendo // divisor  # Divisão inteira
    resto = dividendo % divisor  # Resto da divisão
    parte_fracionada = resultado_normal - resultado_inteiro  # Parte fracionada
    
    # Apresenta os resultados
    print("Dividendo:", dividendo)
    print("Divisor:", divisor)
    print("Resto:", resto)
    print("Resultado normal:", resultado_normal)
    print("Resultado inteiro:", resultado_inteiro)
    print("Parte fracionada:", parte_fracionada)

# Exemplo de uso
dividendo = 202021565
divisor = 60
calcular_divisao(dividendo, divisor)
