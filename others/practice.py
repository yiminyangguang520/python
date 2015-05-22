__author__ = 'ypw'


# Reverse Words in a String
def reverseWords(s):
    words = s.split(" ")
    s2 = ""
    for i in words[::-1]:
        if len(i) > 0:
            s2 += i + " "
    return s2.strip()


print reverseWords("the sky is blue")
print reverseWords("   a   b ")

