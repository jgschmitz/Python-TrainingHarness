import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance import squareform

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

# Hierarchical clustering
linked = linkage(squareform(matrix), method="average")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# Dendrogram
dendrogram(linked, labels=words, ax=ax1, color_threshold=1.5)
ax1.set_title("Word Cluster Tree")
ax1.set_ylabel("Edit Distance")

# Heatmap
im = ax2.imshow(matrix, cmap="YlOrRd")
plt.colorbar(im, ax=ax2, label="Edit Distance")
ax2.set_xticks(range(n)); ax2.set_xticklabels(words, rotation=45)
ax2.set_yticks(range(n)); ax2.set_yticklabels(words)
for i in range(n):
    for j in range(n):
        ax2.text(j, i, matrix[i, j], ha="center", va="center", fontsize=11)
ax2.set_title("Levenshtein Distance Heatmap")

plt.tight_layout()
plt.show()
