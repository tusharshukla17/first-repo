# CODE 1
# Searching Part
"""
def KMPSearch(txt, ptrn):
    N = len(txt)
    M = len(ptrn)
    lps = [0]*M #Longest Preffix & Suffix

    i = 0
    j = 0

    computeLPSArray(ptrn, M ,lps)

    while i<N:
        if txt[i] == ptrn[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == M:
            print("Output from CODE 1")
            print("Pattern Found at: ", str(i-j))
            j = lps[j-1]

def computeLPSArray(ptrn, M, lps):
    len = 0
    i = 1
    lps[0] = 0

    while i<M:
        if ptrn[i] == ptrn[len]:
            lps[i] = len + 1
            len += 1
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1

txt = "abcdefghi"
ptrn = "abc"
print(KMPSearch(txt,  ptrn))


#CODE 2
def KMPSearch(ptrn, txt):
    M = len(ptrn)
    N = len(txt)
    
    #create lps[] that will hold the longest prefix and sufix values for pattern
    lps = [0]*M
    j = 0 #index of pattern

    #preprocess the pattern (calculate lps[] array)
    computeLPSArray(ptrn, M, lps)

    i = 0#index for text
    
    while i<N:
        if ptrn[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            print("Output from CODE 2")
            print("Patternt found at: " + str(i-j))
            j = lps[j-1]
        #Missmatch after j matches 
        elif i<N and ptrn[j] != txt[i]:
            #Do not match lps[0..lps[j-1]] characters, they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

def computeLPSArray(ptrn, M, lps):
    len = 0#lenth of longest prefix and suffix
    i = 1
    lps[0] #lps[0] is allways 0

    #the loops calculate lps[i] for i = 1 to M - 1
    while i<M:
        if ptrn[i] == ptrn[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            #This is not tricky. consider the example
            # AAACAAA and i = 7. the idea is similar to search step
            if len != 0:
                len = lps[len-1]
                #also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

txt = "ABABDABACDABABCABAB"
ptrn = "ABABCABAB"
print(KMPSearch(ptrn, txt)) 



"""


def kmpSearch(ptrn, txt):
    N = len(txt)
    M = len(ptrn)

    lps = [0]*M
    i = 0
    j = 0

    computeLPSarray(ptrn, M, lps)

    while i < N:
        if ptrn[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            print("Pattern Found at: " + str(i-j))
            j = lps[j-1]
        elif i < N and ptrn[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


def computeLPSarray(ptrn, M, lps):
    len = 0
    i = 1
    lps[0]

    while i < M:
        if ptrn[i] == ptrn[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1


txt = "tusharshukla"
ptrn = "shukla"
print(kmpSearch(ptrn, txt))
