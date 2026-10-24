"""Erzeugt die Material-Raster der Bibliothek (Provenienz: dieses Skript, prozedural, keine Fremdbilder).
linen.png      – nahtlose Buchleinen-Kachel, neutral grau, fuer multiply-Ueberlagerung (256x256, Anzeige 128 pt @2x)
praegung.png   – eine goldene Praegelinie, senkrecht (8x224, Anzeige 4x112 pt)
vorsatz.png    – marmoriertes Vorsatzpapier (Sepia, wenig Gold), nahtlos horizontal (780x48, Anzeige 390x24 pt)
"""
import numpy as np
from PIL import Image, ImageFilter
rng = np.random.default_rng(7)
out = __file__.rsplit('/', 1)[0] + '/'

# Leinen: Kett- und Schussfaeden mit leichter Unregelmaessigkeit, kachelbar
N = 256
y, x = np.mgrid[0:N, 0:N]
warp = 0.5 + 0.5 * np.sin(2 * np.pi * x / 6 + rng.normal(0, .6, (1, N)).cumsum(1) * .05)
weft = 0.5 + 0.5 * np.sin(2 * np.pi * y / 6 + rng.normal(0, .6, (N, 1)).cumsum(0) * .05)
slub_x = np.repeat(rng.normal(0, 1, (1, N)), N, 0); slub_y = np.repeat(rng.normal(0, 1, (N, 1)), N, 1)
grain = rng.normal(0, 1, (N, N))
v = 0.5 * np.where((x // 3 + y // 3) % 2 == 0, warp, weft) + 0.14 * slub_x + 0.14 * slub_y + 0.08 * grain
v = (v - v.min()) / (v.max() - v.min())
lum = 196 + 59 * v            # hell: multiply dunkelt die Grundfarbe nur leicht ab
Image.fromarray(lum.astype('uint8'), 'L').filter(ImageFilter.GaussianBlur(0.35)).convert('RGB').save(out + 'linen.png')

# Praegelinie Gold: Folienglanz mit Kanten
W, H = 8, 224
col = np.zeros((H, W, 4), 'uint8')
t = np.linspace(0, 1, H)[:, None]
shine = 0.75 + 0.25 * np.sin(t * 9 + 1.3)
base = np.array([201, 162, 74]); hi = np.array([243, 219, 150])
for i in range(W):
    edge = 1 - abs((i - (W - 1) / 2) / ((W - 1) / 2))
    c = base + (hi - base) * (shine * edge)
    col[:, i, :3] = np.clip(c, 0, 255)
    col[:, i, 3] = int(255 * min(1, edge * 1.8))
Image.fromarray(col, 'RGBA').save(out + 'praegung.png')

# Vorsatzpapier: ruhiger Papiergrund mit feinen, verwirbelten Marmoradern in Sepia und wenig Gold, horizontal kachelbar
W, H = 780, 48
yy, xx = np.mgrid[0:H, 0:W].astype(float)
ph = 2 * np.pi * xx / W
warp = sum(a * np.sin(ph * f + p0 + yy / H * q) for a, f, p0, q in [(6, 2, .3, 1.1), (3, 5, 1.7, 2.3), (1.5, 13, .9, 3.1), (.7, 29, 2.2, 1.7)])
field = yy + warp
ground = np.array([239, 233, 222], float)
img = np.tile(ground, (H, W, 1))
for spacing, width, col, alpha in [(9.0, .9, np.array([120, 92, 66.]), .45), (23.0, .6, np.array([176, 140, 70.]), .55)]:
    d = np.abs(((field / spacing) % 1) - .5) * spacing
    a = np.clip(1 - d / width, 0, 1) * alpha + np.clip(1 - d / (width * 4), 0, 1) * alpha * .15
    img = img * (1 - a[..., None]) + col * a[..., None]
Image.fromarray(img.clip(0, 255).astype('uint8'), 'RGB').filter(ImageFilter.GaussianBlur(0.45)).save(out + 'vorsatz.png')
print('ok')
