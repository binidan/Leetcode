def isPalindrome(x: int):
        num = str(x)
        l=len(num)
        for i in range(l//2):
            if num[i] != num[l-1-i]:
                return False
        return True

print(isPalindrome(212))