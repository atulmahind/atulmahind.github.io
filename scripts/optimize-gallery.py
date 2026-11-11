"""Regenerate gallery WebP variants: python3 -m pip install Pillow==13.0.0."""

from pathlib import Path

from PIL import Image, ImageOps


gallery = Path(__file__).resolve().parents[1] / "assets/img/fine-art"
for source in sorted(gallery.glob("*.jpg")):
    with Image.open(source) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
        for width in (400, 800, 1110):
            height = round(image.height * width / image.width)
            resized = image.resize((width, height), Image.Resampling.LANCZOS)
            destination = source.with_name(f"{source.stem}-{width}.webp")
            resized.save(destination, "WEBP", quality=82, method=6)
            print(f"{destination.name}: {destination.stat().st_size:,} bytes")
