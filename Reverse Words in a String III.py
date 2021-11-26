def reverseWords(s):
    s = s.split()
    c = ''
    for i in s :
        c += ' '+ i[::-1]
    return c.lstrip()

"""
Runtime: 42 ms, faster than 51.50% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 15 MB, less than 48.36% of Python3 online submissions for Reverse Words in a String III.
"""





a1 = "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"
b1 = "God Ding"
#Output: "doG gniD"
print(reverseWords(a1))