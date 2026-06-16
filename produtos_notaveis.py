import time
import sympy as sp

def demonstrar_produtos_notaveis():
    print("=" * 60)
    print("MATEMÁTICA COMPUTACIONAL: PRODUTOS NOTÁVEIS EM PYTHON")
    print("=" * 60)
    
    # 1. Demonstração Simbólica (Álgebra Computacional)
    a, b = sp.symbols('a b')
    expressao = (a + b)**2
    expressao_expandida = sp.expand(expressao)
    
    print(f"\n[Simbólico] Expressão Base: ({a} + {b})²")
    print(f"[Simbólico] Forma Expandida Computacional: {expressao_expandida}")
    
    # 2. Análise Numérica de Desempenho (Grandes Números)
    x_val, y_val = 987654, 123456
    
    # Abordagem Otimizada: (x + y)**2
    inicio_otimizado = time.perf_counter()
    resultado_otimizado = (x_val + y_val) ** 2
    fim_otimizado = time.perf_counter()
    tempo_otimizado = fim_otimizado - inicio_otimizado
    
    # Abordagem Tradicional Expandida: x² + 2xy + b²
    inicio_expandido = time.perf_counter()
    resultado_expandido = (x_val ** 2) + (2 * x_val * y_val) + (y_val ** 2)
    fim_expandido = time.perf_counter()
    tempo_expandido = fim_expandido - inicio_expandido
    
    print(f"\n[Numérico] Avaliando para a={x_val} e b={y_val}:")
    print(f"-> Tempo Forma Simplificada: {tempo_otimizado:.8f} segundos")
    print(f"-> Tempo Forma Expandida:    {tempo_expandido:.8f} segundos")
    print(f"-> Os resultados batem? {resultado_otimizado == resultado_expandido}")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    demonstrar_produtos_notaveis()