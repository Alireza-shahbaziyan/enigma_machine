from random import shuffle
import pickle
#Enigma 
masterbet = "abcdefghijklmnopqrstuvwxyz"

# rotor 1
r1 = list(masterbet)
shuffle(r1)
r1 = ''.join(r1)

# rotor 2
r2 = list(masterbet)
shuffle(r2)
r2 = ''.join(r2)

# rotor 3
r3 = list(masterbet)
shuffle(r3)
r3 = ''.join(r3)

f = open("rotor_state","wb")
pickle.dump((r1,r2,r3), f )
f.close()

