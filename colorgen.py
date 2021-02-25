import matplotlib.pyplot as plt

colors = plt.get_cmap("twilight")

for c in colors.colors:
    print("color.RGBA{{0x{:02x}, 0x{:02x}, 0x{:02x}, 0xff}},".format(int(c[0]*255),int(c[1]*255),int(c[2]*255)))

# for c in range(0, 256):
#     print("color.RGBA{{0x{:02x}, 0x{:02x}, 0x{:02x}, 0xff}},".format(c, c, c))