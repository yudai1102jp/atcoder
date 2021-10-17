s=input()
s2=s[:((len(s)-1)//2)]
s3=s[(len(s)+1)//2:len(s)]

bool=1
if not s==s[::-1]:
    bool=0
if not s2==s2[::-1]:
    bool=0
if not s3==s3[::-1]:
    bool=0

if bool:
    print("Yes")
else:
    print("No")