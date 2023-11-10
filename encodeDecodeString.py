class Solution:
    def encode(self, strs):
        ans = ""
        for curr in strs:
            ans += str(len(curr)) + "#" + curr
        return ans

    def decode(self, original_string):
        ans = []
        while original_string:
            res = original_string.split("#", 1)
            strLen = int(res[0])
            original_string = res[1]
            ans.append(original_string[:strLen])
            original_string = original_string[strLen:]

        return ans

unicode_string1 = "AbC123!@#"
unicode_string2 = "Xyz789*&^"
unicode_string3 = "PQR456~`"
unicode_string4 = "uvw12()[]"

# Create a list of strings
unicode_strings = [unicode_string1, unicode_string2, unicode_string3, unicode_string4]
print(unicode_strings)
encodedStr = Solution().encode(unicode_strings)
decodedStrs = print(Solution().decode(encodedStr))
