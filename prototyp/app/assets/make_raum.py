"""Raum-Raster der Startseite (Provenienz: dieses Skript, prozedural, keine Fremdbilder).
rueckwand.png  – Regal-Rueckwand aus ungebleichtem Papier/Rohleinen, warm, nahtlos (256x256, Anzeige 128 pt)
papier.png     – helles warmes Buchpapier fuer Buchseiten und Sheets, nahtlos (256x256)
brett.png      – Regalbrett aus hellem Holz mit Vorderkante (780x36, Anzeige 390x18 pt)
baendchen.png  – Lesebaendchen aus rotem Seidenrips mit Schwalbenschwanz (24x160, Anzeige 12x80 pt)
"""
import numpy as np
from PIL import Image, ImageFilter
rng = np.random.default_rng(11)
out = __file__.rsplit('/', 1)[0] + '/'

def tile_noise(n, scale):
    # kachelbare Wertrausch-Textur via Fourier-Filter
    f = np.fft.fft2(rng.normal(0, 1, (n, n)))
    ky, kx = np.meshgrid(np.fft.fftfreq(n), np.fft.fftfreq(n), indexing='ij')
    k = np.sqrt(kx ** 2 + ky ** 2) + 1e-6
    v = np.real(np.fft.ifft2(f * np.exp(-(k * scale) ** 2)))
    return (v - v.mean()) / v.std()

N = 256
y, x = np.mgrid[0:N, 0:N]
def paper(base, amp_fibre, amp_cloud, weave):
    fibre = tile_noise(N, 2.0)
    cloud = tile_noise(N, 40.0)
    w = (np.sin(2 * np.pi * x / 4) * np.sin(2 * np.pi * y / 4)) * weave
    lum = fibre * amp_fibre + cloud * amp_cloud + w
    img = np.array(base, float)[None, None, :] + lum[..., None] * np.array([1.0, 0.97, 0.9])
    return Image.fromarray(img.clip(0, 255).astype('uint8'), 'RGB')

paper((233, 223, 204), 3.0, 1.7, 1.4).filter(ImageFilter.GaussianBlur(0.4)).save(out + 'rueckwand.png')
paper((248, 244, 235), 2.0, 1.6, 0).filter(ImageFilter.GaussianBlur(0.4)).save(out + 'papier.png')

# Regalbrett: Draufsicht-Kante oben hell, Stirnseite mit Maserung, weiche Schattenkante unten
W, H = 780, 36
yy, xx = np.mgrid[0:H, 0:W].astype(float)
g = np.sin(xx / 23 + 2.5 * np.sin(xx / 170) + yy * 0.35) * 5 + rng.normal(0, 2.2, (H, W))
base = np.array([196, 168, 128], float)
img = np.tile(base, (H, W, 1)) + g[..., None] * np.array([1, .85, .6])
img[:7] = np.array([214, 190, 152]) + g[:7, :, None] * .4      # Oberseite
img[7:8] = np.array([168, 138, 98])                              # Kante
img[28:] = img[28:] * np.linspace(1, .78, 8)[:, None, None]     # Unterkante
rgba = np.dstack([img.clip(0, 255), np.full((H, W), 255.)])
Image.fromarray(rgba.astype('uint8'), 'RGBA').filter(ImageFilter.GaussianBlur(0.4)).save(out + 'brett.png')

# Lesebaendchen: Rips mit Glanz, Schwalbenschwanz unten
W, H = 24, 160
yy, xx = np.mgrid[0:H, 0:W].astype(float)
rib = 0.5 + 0.5 * np.sin(yy * 1.9)
sheen = 1 - np.abs((xx - W / 2) / (W / 2)) ** 2
c = np.array([132, 30, 26.]) + (np.array([178, 52, 44.]) - np.array([132, 30, 26.])) * (0.55 * sheen[..., None] + 0.2 * rib[..., None])
a = np.ones((H, W)) * 255
notch = (yy > H - 22) & (np.abs(xx - W / 2) < (yy - (H - 22)) * 0.55)
a[notch] = 0
a[:, :1] = 160; a[:, -1:] = 160
Image.fromarray(np.dstack([c.clip(0, 255), a]).astype('uint8'), 'RGBA').save(out + 'baendchen.png')
print('ok')
