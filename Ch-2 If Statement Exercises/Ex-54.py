wv = float(input("Enter the wavelength of the wave in nano-meters: "))
if wv < 380:
    print("This wavelength is not visible.")
elif wv >= 380 and wv < 450:
    print("This wavelength is violet.")
elif wv >= 450 and wv < 495:
    print("This wavelength is blue.")
elif wv >= 495 and wv < 570:
    print("This wavelength is green.")
elif wv >= 570 and wv < 590:
    print("This wavelength is yellow.")
elif wv >= 590 and wv < 620:
    print("This wavelength is orange.")
elif wv >= 620 and wv < 750:
    print("This wavelength is red.")
else:
    print("This wavelength is not visible.")
    