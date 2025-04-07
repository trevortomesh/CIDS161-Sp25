def gcd(n1, n2):
    gcd = 1 # Initial value
    k = 2 # first possible GCD other than 1

    while k <= n1 and k <=n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k # update gcd

        k += 1
    return gcd