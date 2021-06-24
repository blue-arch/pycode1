class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        dp = [[i for j in range(K + 1)] for i in range(N + 1)]

        for j in range(K + 1):
            dp[0][j] = 0

        dp[1][0] = 0
        for j in range(K + 1):
            dp[1][j] = 1

        for i in range(N + 1):
            dp[i][0] = 0
            dp[i][1] = i

        data = []
        for i in range(2, N + 1):
            for j in range(2, K + 1):
                for k in range(1, i + 1):
                    # 把最后一行，最后一列的求解过程制作成图表
                    if i == N and j == K:
                        data.append([k, dp[k - 1][j - 1], dp[i - k][j]])
                    dp[i][j] = min(dp[i][j], max(dp[k - 1][j - 1], dp[i - k][j]) + 1)
        return dp[N][K], data


solution = Solution()
K = 3
N = 14
res, data = solution.superEggDrop(K, N)
import pandas as pd

scatters = pd.DataFrame(data=data, columns=['k','dp[k - 1][j - 1]','dp[i - k][j]'])

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
plt.scatter(
    scatters['k'], scatters['dp[k - 1][j - 1]'], c='r', marker='o', s=200)
plt.scatter(scatters['k'], scatters['dp[i - k][j]'], c='g', marker='*', s=300)
plt.legend(loc='upper left', prop={'size': 18})

plt.xticks([i for i in range(len(data) + 1)])
plt.tick_params(labelsize=14)
plt.title('$N = 14, K = 3$', size=20)
plt.ylabel('dp value', size=14)
plt.xlabel('$k$', size=14)
plt.grid()
plt.savefig("image.png")

