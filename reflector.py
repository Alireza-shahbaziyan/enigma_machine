from pickle import load

masterbet = "abcdefghijklmnopqrstuvwxyz"
f= open('./rotor_state','rb')
r1,r2,r3=load(f)
f.close()

def Reflector(char):       
        location_char = masterbet.find(char)
        revers_masterbet  = masterbet[::-1]
        return revers_masterbet[location_char]

def Enigma_one_char(c):
    c1 = r1[masterbet.find(c)]
    c2 = r2[masterbet.find(c1)]
    c3 = r3[masterbet.find(c2)]
    reflected = Reflector(c3)
    c3 = masterbet[r3.find(reflected)]
    c2 = masterbet[r2.find(c3)]
    c1 = masterbet[r1.find(c2)]
    return c1

def rotet_rotor():
    global r1,r2,r3
    r1 = r1[1:]+r1[0]
    if state % 26:
        r2 = r2[1:]+r2[0]
        if state % 676 : 
            r3 = r3[1:]+r3[0]


text = "hihihihihi"
cipher = ''
state = 0

for c in text:
    state +=1
    cipher += Enigma_one_char(c)
    rotet_rotor()


print(cipher)