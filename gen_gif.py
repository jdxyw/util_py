import imageio

numFile = 17

files = [
    "/Users/yongweixing/fake_samples_epoch_%03d.png" % (i)
    for i in range(1, numFile)
]

imgs = []

for f in files:
    imgs.append(imageio.imread(f))

imageio.mimsave("./fake_images_gan.gif", imgs, 'GIF', duration=0.5)
