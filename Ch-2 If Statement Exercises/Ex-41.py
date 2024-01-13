name = input("Enter the note name: ")
note = name[0]
octave = int(name[1])
if note == "C":
    freq = 261.63
elif note == "D":
    freq = 293.66
elif note == "E":
    freq = 329.63
elif note == "F":
    freq = 349.23
elif note == "G":
    freq = 392.00
elif note == "A":
    freq = 440.00
elif note == "B":
    freq = 493.88


freq = freq / 2 ** (4 - octave)
print(f"The frequency of {name} is {freq} Hz.")