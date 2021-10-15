def numTeams(rating):
    ans = 0
    n = len(rating)
    #increasing[i][j] denotes the num of teams ending at soldier i with length of j in the order of increasing rating.
    increasing = [[0] * 4 for _ in range(n)]
    #decreasing[i][j] denotes the num of teams ending at soldier i with length of j in the order of decreasing rating.
    decreasing = [[0] * 4 for _ in range(n)]
    #Final answer = (increasing[i][3] + decreasing[i][3]) for i in [0, n - 1].
    for i in range(n):
        for j in range(i):
            if rating[j] < rating[i]:
                increasing[i][2] += 1
                increasing[i][3] += increasing[j][2]
            else:
                decreasing[i][2] += 1
                decreasing[i][3] += decreasing[j][2]
        ans += increasing[i][3] + decreasing[i][3]
    return ans
