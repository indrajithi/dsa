class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        return s[::-1]

    def reverseStringInplace(self, s):
        """
        Reverse the string inplace
        """
        start = 0
        end = len(s) - 1

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    s = Solution()
    string_list = list('hello!')
    print("reverse by copy:", s.reverseString(string_list))

    s.reverseStringInplace(string_list)
    print("reverse inplace:", string_list)
