'''
0! = 1
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
'
'
n! = * (n-1)!
'''

angka = int(input("Masukkan angka: "))
def faktorial(n):
  if n == 0:
      return 1
  else:
      return n * faktorial(n - 1)

print(f"faktorial {angka} adalah {faktorial(angka)}")

