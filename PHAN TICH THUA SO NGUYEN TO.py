def prime_factors(n):
    factors = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
            n //= i
        i += 1

    if n > 1:
        factors[n] = 1

    return factors


def print_prime_factorization(n):
    factors = prime_factors(n)
    result = "1"
    for factor, exponent in factors.items():
        result += f" * {factor}^{exponent}"

    print(result)


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        N = int(input())
        print_prime_factorization(N)
