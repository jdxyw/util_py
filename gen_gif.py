import imageio

numFile = 14

files = ["fake_samples_epoch_%03d.png" % (i) for i in range(1, numFile)]

imgs = []

for f in files:
    imgs.append(imageio.imread(f))

imageio.mimsave("./fake_images_gan.gif", imgs, 'GIF', duration=0.5)
