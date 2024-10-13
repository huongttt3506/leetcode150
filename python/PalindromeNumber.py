class PalindromeNumber:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        for i in range(0,n//2,1):
            if s[i] != s[n-i-1]:
                return False
        return True