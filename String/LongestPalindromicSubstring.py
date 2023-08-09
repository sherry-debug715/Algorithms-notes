class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            print("\nChecking for palindrome at index:", i)

            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print("Checking for odd-length palindrome. Current l and r:", l, r)
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            print("Finished checking for odd-length palindrome at index", i)

            # even length
            l, r = i, i + 1
            print("start to check even length, l and r", l, r)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                print("Checking for even-length palindrome. Current l and r:", l, r)
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            print("Finished checking for even-length palindrome at index", i)

        print("Finished checking all indices. The longest palindrome is:", res)
        return res

test = Solution()
s = "babab"
test.longestPalindrome(s)
