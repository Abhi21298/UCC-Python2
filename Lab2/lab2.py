## Lab 2
import re 

## Question 1
def moolah(s):
    if s==None or s=="":
        return []
    track = []
    pattern = r"EUR( )?[0-9]+(\.[0-9]+)?"
    regexp = re.compile(pattern)
    for m in regexp.finditer(s):
        track.append(m.group())
    
    return track

print(moolah("EUR100 123 EUR 250 EUR 12.50 EUR1000000 000"))

## Question 2
def bleep(s):
    if s==None or s=="":
        return ""
    pattern = r"(^|\b)([a-zA-Z]){4}(\b|$)"
    regexp = re.compile(pattern)
    new_str = regexp.sub(lambda m: "*"*len(m.group()), s)

    return new_str


print(bleep("Fast and the Furious : FOUR"))

## Question 3
def helper(s):
    nums_track = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    l = len(s) - 1
    new_s = []
    new_s.append(s)
    new_s.append(" (")
    for i in range(l):
        new_s.append(str(nums_track[s[i]]+" "))
    new_s.append(str(nums_track[s[l]]+")"))
    del nums_track
    return ''.join(new_s)
        

def to_english(s):
    if s==None or s=="":
        return ""
    pattern = r"(^|\b)[0-9]+(\b|$)"
    regexp = re.compile(pattern)
    new_str = regexp.sub(lambda m: helper(m.group()), s)
    print(new_str)

to_english("My favourite number is 017 and 090!")

## Question 4
def harvest_emails(s):
    if s==None or s=="":
        return ""
    list_emails = []

    #pattern = r"(^|\b)([a-zA-Z0-9_](\.)?)+[a-zA-Z0-9_]+@(([a-z0-9]+(\-)?[a-z0-9]+)+\.)+[a-z0-9]+(\-)?[a-z0-9]+[^\-]($|\b)"
    pattern = r"^[a-zA-Z0-9_]+(\.[a-zA-Z0-9_]+)*@[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9](\.[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9])+$"
    regexp = re.compile(pattern)
    words = list(s.split(' '))

    for word in words:
        obj = regexp.search(word)
        if obj!=None:
            list_emails.append(obj.group())
            obj = None
    #for m in regexp.finditer(s):
    #    list_emails.append(m.group())
    
    return list_emails
    

print(harvest_emails("my name is J.P.Murphy3@c-s.ucc.ie and J.P.Murphy3@c-s.ucc.ie. and however this is invalid \
                     J.P.Murphy3@c-s.ucc.ie  "))