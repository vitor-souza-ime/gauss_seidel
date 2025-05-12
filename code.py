#Matriz admitância 3x3
import numpy as np
import time

# Função de Gauss-Seidel
def gauss_seidel(Y, V0, I, tol=1e-6, max_iter=50):
    V = V0.copy()
    n = len(V)
    iter_count = 0  # Contador de iterações

    for k in range(max_iter):
        iter_count += 1  # Incrementar a cada iteração
        V_old = V.copy()

        # Atualizar as tensões usando o método de Gauss-Seidel
        for i in range(n):
            soma = np.dot(Y[i, :], V) - Y[i, i] * V[i]
            V[i] = (I[i] - soma) / Y[i, i]

        # Verificar se a solução convergiu
        if np.linalg.norm(V - V_old) < tol:
            break

    return V, iter_count

# Definindo a matriz admitância
Y = np.array([[0.1-0.2j, -0.1j, -0.1j],
              [-0.1j, 0.2-0.3j, -0.1j],
              [-0.1j, -0.1j, 0.2-0.2j]])

# Definindo o vetor de corrente
I = np.array([1, 0.8, 1.2])

# Tensões iniciais
V0 = np.array([1+0j, 1+0j, 1+0j])

# Medir o tempo de execução do método Gauss-Seidel
start_time = time.time()
V_gauss, iter_gauss = gauss_seidel(Y, V0, I)
end_time = time.time()

# Exibir os resultados em formato retangular e polar
print("Tensões calculadas (Gauss-Seidel):")
for i, v in enumerate(V_gauss):
    print(f"Tensão {i+1} (Retangular): {v:.2f}")
    print(f"Tensão {i+1} (Polar): {np.abs(v):.2f} ∠{np.degrees(np.angle(v)):.2f}°")
print("Iterações (Gauss-Seidel):", iter_gauss)
print("Tempo de execução (Gauss-Seidel):", end_time - start_time, "segundos")
