# Две старушки идут навстречу друг другу с постоянными скоростями V1 и V2 км/ч.
# Определите, через какое время старушки встретятся, если расстояние между
# ними равно S км.


S, V1, V2 = float(input()), float(input()), float(input())
t = S / (V1 + V2)
print(t)
