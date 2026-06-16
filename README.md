# 📐 Matemática Computacional: Otimização com Produtos Notáveis

Este repositório foi criado para centralizar meus estudos e experimentos práticos na disciplina de **Matemática Computacional** durante a minha graduação em Ciência da Computação. 

O objetivo principal é demonstrar como conceitos matemáticos abstratos afetam diretamente a performance, a arquitetura de software e os ciclos de processamento de CPU no dia a dia da programação.

---

## 💡 O Conceito: Produtos Notáveis vs. Performance

Muitas vezes, a otimização de um sistema começa na simplificação algébrica antes mesmo de digitarmos a primeira linha de código. Para ilustrar isso, este projeto analisa o impacto computacional do **Quadrado da Soma de Dois Termos**:

$$\mathbf{(a + b)^2 = a^2 + 2ab + b^2}$$

### Análise de Ciclos de CPU:
* **Forma Otimizada $(a + b)^2$:** Exige apenas **1 Adição** e **1 Multiplicação (Potência)**.
* **Forma Expandida $a^2 + 2ab + b^2$:** Exige **2 Multiplicações**, **2 Potências** e **2 Adições**.

Em cenários de alta concorrência, processamento de imagens, Big Data ou Criptografia, essa diferença matemática economiza microsegundos preciosos de hardware.

---

## 🐍 Implementação em Python

O script `produtos_notaveis.py` utiliza duas abordagens:
1. **Computação Simbólica:** Usa a biblioteca `SymPy` para demonstrar a expansão algébrica de forma pura.
2. **Análise Numérica Empírica:** Usa a biblioteca `time` para mensurar o tempo de execução de ambas as formas com valores numéricos massivos.

### Pré-requisitos
Para rodar o script localmente, certifique-se de ter o Python instalado e instale a biblioteca de computação simbólica:
```bash
pip install sympy
