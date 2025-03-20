def isPalindrome(n):
    
    if str(n) == str(n)[::-1]: # Para ler um numero de tras pra frente em Python, converte o numero para string e inverte a string usando [::-1]
        return True
    else: 
        return False

print(isPalindrome(121))