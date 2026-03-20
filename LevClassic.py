import matplotlib.pyplot as plt
import numpy as np

def levenshtein(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]

words = ["cat", "car", "bar", "bat", "hat", "hot", "dog", "log"]
n = len(words)
matrix = np.array([[levenshtein(w1, w2) for w2 in words] for w1 in words])

plt.figure(figsize=(6, 5))
plt.imshow(matrix, cmap="YlOrRd")
plt.colorbar(label="Edit Distance")
plt.xticks(range(n), words, rotation=45)
plt.yticks(range(n), words)
for i in range(n):
    for j in range(n):
        plt.text(j, i, matrix[i, j], ha="center", va="center", fontsize=11)
plt.title("Levenshtein Distance Heatmap")
plt.tight_layout()
plt.show()
