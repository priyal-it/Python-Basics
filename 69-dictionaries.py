#lec 5.1: Dictionaries
d={}
d['pari']=9696969696
d['ramya']=4545454545
d['riya']=3434343434
print(d['ramya'])

s='it was monday morning swaminathan was reluctant to open his eyes he considered monday specially unpleasant in the calendar after the delicious freedom of saturday and sunday it was difficult to get into the monday mood of work and discipline he shuddered at the very thought of school that dismal yellow building the fire-eyed vedanayagam his class-teacher and the head master with his thin long cane'

words=s.split(" ")
malgudi={}
for word in set(words):
    malgudi=dict.fromkeys(set(words), 0)

for word in words:
    if word in malgudi:
        malgudi[word]+=1

print(malgudi)

max_count=0
for x in malgudi:
    if malgudi[x]>max_count:
        max_count=malgudi[x]

for x in malgudi:
    if malgudi[x]==max_count:
        max_count_word=x

print("\'{0}\' is repeated {1} times which is the maximum".format(max_count_word,max_count))