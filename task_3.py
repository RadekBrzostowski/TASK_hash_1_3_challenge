words = "Hey there mate, it's nice to finally meet you!"
# words = "Idzie grzes przez wies i tak sobie czyta co to jes tak to sprawdzic jaki to jest dlugi napis tu sie zrobil ze chu chu chu!"
maximum_width = 15
out_words = []
start = 0
# initial variable


while len(words[start:]) > maximum_width:                       # spliting by <space> before maximum

    words_rfind = words[start:maximum_width+start].rfind(" ")   # where is <space> in range of start and width
    words_width = words[start:words_rfind+start]                # string for one line/row
    start += words_rfind +1                                     # next start idx
    out_words.append(words_width)                               # make list of row


for x in range(0, len(out_words)):                              # iteration 
    t = 1                                                       # multiplier for oldvalue. New value is +1
    temp_out = out_words[x]                                     # temporary out
    space_count = out_words[x].count(" ")                       # <space> counter
    while len(temp_out) < maximum_width:                        # a loop that extends the string 
        for tt in range(space_count):                           # tt - number of the value to replace
            temp_out = out_words[x].replace(" " * t, " " * (t+1), tt+1)     # replace short <space> to +1
            if len(temp_out) == maximum_width:                              # maybe done ?
                break                                                       # .........
        t += 1                                                              # one more <space>
        out_words[x] = temp_out                                             

# print(len(out_words))
out_words.append(words[start:])                                             # last row append
print("out:  ")
print(out_words)

for u in out_words:
    print(u)
