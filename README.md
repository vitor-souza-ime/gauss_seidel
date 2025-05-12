
````markdown
# Método de Gauss-Seidel para Análise de Sistemas Elétricos de Potência

Este projeto apresenta uma implementação computacional do método iterativo de **Gauss-Seidel** para o cálculo de tensões nodais em sistemas elétricos de potência, utilizando uma matriz admitância (Y) e um vetor de corrente (I) como entrada.

## 📋 Descrição

O método de Gauss-Seidel é uma técnica numérica iterativa amplamente utilizada na análise de fluxo de carga em sistemas de potência. Esta implementação:

- Utiliza uma matriz admitância \( Y \) 3x3 com valores complexos;
- Aplica o método de Gauss-Seidel para obter as tensões \( V \) nos nós do sistema;
- Converge para a solução dentro de uma tolerância especificada ou até um número máximo de iterações;
- Apresenta as tensões resultantes em forma retangular e polar;
- Mede o tempo de execução do algoritmo.

## 🧮 Fórmula

A atualização da tensão em cada iteração segue a equação:

\[
V_i^{(k+1)} = \frac{1}{Y_{ii}} \left( I_i - \sum_{j \neq i} Y_{ij} \cdot V_j^{(k)} \right)
\]

## 🚀 Como executar

Certifique-se de ter o Python instalado em sua máquina. Instale também o pacote NumPy:

```bash
pip install numpy
````

Execute o script:

```bash
python gauss_seidel_potencia.py
```

## 🧾 Exemplo de entrada

```python
Y = np.array([[0.1-0.2j, -0.1j, -0.1j],
              [-0.1j, 0.2-0.3j, -0.1j],
              [-0.1j, -0.1j, 0.2-0.2j]])

I = np.array([1, 0.8, 1.2])
V0 = np.array([1+0j, 1+0j, 1+0j])
```

## 📌 Saída esperada

```text
Tensões calculadas (Gauss-Seidel):
Tensão 1 (Retangular): ...
Tensão 1 (Polar): ... ∠...°
...
Iterações (Gauss-Seidel): N
Tempo de execução (Gauss-Seidel): ... segundos
```

## 📚 Referências

* Stevenson, W. D. *Elementos de Análise de Sistemas de Potência*.
* Glover, J. D., Sarma, M. S. *Power System Analysis and Design*.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Sinta-se à vontade para utilizar e modificar.


