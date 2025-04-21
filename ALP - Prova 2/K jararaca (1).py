n = int(input())
palindromes = []

for i in range(n):
    name = input().strip()
    if name == name[::-1]:
        palindromes.append(name)

for palindrome in palindromes:
    print(palindrome)

