"""Split Steve's 4-up roll-up mock into single exterior frames and copy the interior plate."""
from PIL import Image
import numpy as np

root = __import__('pathlib').Path(__file__).resolve().parents[1]
src = root / 'assets' / 'source'
out = root / 'assets' / 'img'
out.mkdir(parents=True, exist_ok=True)

mock = Image.open(src / 'rollup-mock.jpeg')
rows = np.array(mock.convert('L')).mean(axis=1) < 25
bands, start = [], None
for i, dark in enumerate(list(rows) + [True]):
    if not dark and start is None:
        start = i
    elif dark and start is not None:
        bands.append((start, i)); start = None

names = ['exterior-door-closed', 'exterior-door-40', 'exterior-door-75', 'exterior-door-100']
for (a, b), name in zip(bands, names):
    mock.crop((0, a, mock.width, b)).save(out / f'{name}.jpg', quality=90)
    print(name, (0, a, mock.width, b))

Image.open(src / 'hero-mid-door-interior.jpeg').save(out / 'interior-wide.jpg', quality=90)
print('interior-wide', 'ok')
