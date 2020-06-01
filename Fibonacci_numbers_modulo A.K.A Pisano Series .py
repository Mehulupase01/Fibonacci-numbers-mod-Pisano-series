# python3
#createdby Mehul Upase

def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
       return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def Pisanoperiodno(m):
   assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
   a=0
   b=1
   for i in range(0,m*m):
       c=(a+b)%m
       a=b
       b=c
       if a==0 and b==1:
        return i+1
def Fmodmcalc(n,m):
     # Getting the period
    pisano_period = Pisanoperiodno(m)

    # Taking mod of N with
    # period length
    n = n % pisano_period

    previous, current = 0, 1
    if n==0:
        return 0
    elif n==1:
        return 1
    for i in range(n-1):
        previous, current \
        = current, previous + current

    return (current % m)


if __name__ == '__main__':
    input_n,input_m= map(int, input().split())
    if input_n<1:
        print(0)
    if input_n==1:
        print(1)
    elif input_n>=2:
      n=input_n
      m=input_m
      print(Fmodmcalc(n,m))
