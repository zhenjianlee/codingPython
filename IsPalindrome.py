import re

line="  Able was I, ere, I saw Elba  "
line2= "I really need to get a job soon! Oh my god!!!"

def isPalindrome(s):
    s=s.strip().lower()
    s=re.sub(r'[^a-zA-Z0-9]','',s)
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

print(line+" : "+ str(isPalindrome(line)))
print(line2+" : "+ str(isPalindrome(line2)))